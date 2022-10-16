//
//  QuestionsVController.swift
//  TextClassification
//
//  Created by Abraham Collins on 10/16/22.
//  Copyright © 2022 Google Inc. All rights reserved.
//

import UIKit
import SwiftUI

@available(iOS 13.0, *)

class QuestionsVController: UIViewController {
    
    @IBOutlet weak var firstquestion: UIButton!
    @IBOutlet weak var secondquestion: UIButton!
    @IBOutlet weak var thirdquestion: UIButton!
    @IBOutlet weak var fourthquestion: UIButton!
    
    private var scores: [String] = []
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupButtons1()
        setupButtons2()
        setupButtons3()
        setupButtons4()
        
        
        
        //["1: Strongly relate","2: Moderately relate","3: Mildly relate","4: Slightly relate","5: Don't relate"]

        // Do any additional setup after loading the view.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */
    
    func setupButtons1(){
        let optionClosure = {(action:UIAction) in
            //scores[0] = action.title.first
            print(action.title)}
        
        firstquestion.menu = UIMenu(children: [
            UIAction(title:"1: Strongly relate", state: .on, handler: optionClosure),
            UIAction(title:"2: Moderately relate", handler: optionClosure),
            UIAction(title:"3: Mildly relate", handler: optionClosure),
            UIAction(title:"4: Slightly relate", handler: optionClosure),
            UIAction(title:"5: Don't relate", handler: optionClosure)])
            
        firstquestion.showsMenuAsPrimaryAction = true
        firstquestion.changesSelectionAsPrimaryAction=true
        
    }
    
    func setupButtons2(){
        let optionClosure = {(action:UIAction) in
            print(action.title)}
        
        secondquestion.menu = UIMenu(children: [
            UIAction(title:"1: Strongly relate", state: .on, handler: optionClosure),
            UIAction(title:"2: Moderately relate", handler: optionClosure),
            UIAction(title:"3: Mildly relate", handler: optionClosure),
            UIAction(title:"4: Slightly relate", handler: optionClosure),
            UIAction(title:"5: Don't relate", handler: optionClosure)])
            
        secondquestion.showsMenuAsPrimaryAction = true
        secondquestion.changesSelectionAsPrimaryAction=true
        
    }
    
    func setupButtons3(){
        let optionClosure = {(action:UIAction) in
            print(action.title)}
        
        thirdquestion.menu = UIMenu(children: [
            UIAction(title:"1: Strongly relate", state: .on, handler: optionClosure),
            UIAction(title:"2: Moderately relate", handler: optionClosure),
            UIAction(title:"3: Mildly relate", handler: optionClosure),
            UIAction(title:"4: Slightly relate", handler: optionClosure),
            UIAction(title:"5: Don't relate", handler: optionClosure)])
            
        thirdquestion.showsMenuAsPrimaryAction = true
        thirdquestion.changesSelectionAsPrimaryAction=true
        
    }
    
    func setupButtons4(){
        let optionClosure = {(action:UIAction) in
            print(action.title)}
        
        fourthquestion.menu = UIMenu(children: [
            UIAction(title:"1: Strongly relate", state: .on, handler: optionClosure),
            UIAction(title:"2: Moderately relate", handler: optionClosure),
            UIAction(title:"3: Mildly relate", handler: optionClosure),
            UIAction(title:"4: Slightly relate", handler: optionClosure),
            UIAction(title:"5: Don't relate", handler: optionClosure)])
            
        fourthquestion.showsMenuAsPrimaryAction = true
        fourthquestion.changesSelectionAsPrimaryAction=true
        
    }
    
    
    @IBAction func SaveAnswers(_ sender: UIButton) {
        
    }
    

}
