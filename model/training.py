
from this import d
import os
import tensorflow as tf
from tflite_model_maker import model_spec
from tflite_model_maker import text_classifier
from tflite_model_maker.text_classifier import DataLoader
from tflite_support import metadata as _metadata
import argparse

parser = argparse.ArgumentParser(description=' ################ MySafetyNet: Model training ################', usage='%(prog)s')
parser.add_argument('-tr', '--train', type=str, required=True, help='Input csv file containing the training data', dest='train')
parser.add_argument('-va', '--valid', type=str, help='Input csv file containing the validation ata', dest='valid')
parser.add_argument('-te', '--test', type=str, help='Input csv file containing the testing data', dest='test')
parser.add_argument('-m', '--model', type=str, choices=['average_word_vec', 'mobilebert_classifier', 'bert_classifier'], default='mobilebert_classifier', dest='model', help='select model [average_word_vec, mobilebert_classifier, bert_classifier]')
parser.add_argument('-e', '--epochs', type=int, default=10, dest='epochs', help='epochs for training')
parser.add_argument('-out', '--output', type=str, required=True, help='Output path for saving the data', dest='output')

args = parser.parse_args()
train = args.train
valid = args.valid
test = args.test
model = args.model
epochs = args.epoch
out_path = args.output

def load_model(model):
    spec = model_spec.get(model)
    return spec


def load_data(data, model):
    dataset = DataLoader.from_csv(
        filename=data,
        text_column='text',
        label_column='label',
        model_spec=model,
        is_training=True)
    return dataset

def main():
    
    # using mobilebert_classifier
    spec = model_spec.get(model)

    # loading data
    train_data = load_data(train, spec)
    if args.valid:
        valid_data = load_data(valid, spec)
    if args.test:
        test_data = load_data(test, spec)

    # Train
    if args.valid:
        model = text_classifier.create(train_data, 
                                    model_spec=spec,
                                    validation_data=valid_data, 
                                    epochs=epochs)
    else:
        model = text_classifier.create(train_data, 
                                    model_spec=spec,
                                    epochs=epochs)

    model.summary()

    # Test
    if args.valid:
        loss, acc = model.evaluate(test_data)
    
    # Save
    model.export(export_dir=out_path)

    # TFLite model evaluation
    accuracy = model.evaluate_tflite('/content/mobilebert/model.tflite', test_data)
    print('TFLite model accuracy: ', accuracy)

    # Export metadata
    export_model_path='/content/mobilebert/model.tflite'
    displayer = _metadata.MetadataDisplayer.with_model_file(export_model_path)
    print(displayer)
    export_json_file = os.path.join('/content/mobilebert/model.json')
    json_file = displayer.get_metadata_json()
    print(json_file)

    with open(export_json_file, "w") as f:
      f.write(json_file)


if __name__ == "__main__":
    main()