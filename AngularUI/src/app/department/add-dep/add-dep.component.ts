import { Component, OnInit, Input} from '@angular/core';

import {SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-add-dep',
  templateUrl: './add-dep.component.html',
  styleUrls: ['./add-dep.component.css']
})
export class AddDepComponent implements OnInit {

  constructor() { }

  @Input() dep:any;
  DepartmentID:string = "";
  DepartmentName:string = "";
  
  
  ngOnInit(): void {
      this.DepartmentID = this.DepartmentID;
      this.DepartmentName = this.DepartmentName;
  }

  

}
