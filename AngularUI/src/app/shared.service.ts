import { Injectable } from '@angular/core';
import{HttpClient} from '@angular/common/http'
import{Observable} from 'rxjs'

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIUrl = "http://127.0.0.1:8000"
  readonly PhotoUrl = "http://127.0.0.1:8000"

  constructor(private http:HttpClient) {  }
  
  addDepartment(val:any){
    return this.http.post(this.APIUrl + '/department/',val);
  }

  getDepList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/department/');
  }

  updateDepartment(val:any){
    return this.http.put(this.APIUrl + '/department/',val);
  }

  deleteDepartment(val:any){
    return this.http.delete(this.APIUrl + '/department/',val);
  }

  addEmployee(val:any){
    return this.http.post(this.APIUrl + '/employee/',val);
  }
  getEmpList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/employee/');
  }

  updateEmployee(val:any){
    return this.http.put(this.APIUrl + '/employee/',val);
  }
  deleteEmployee(val:any){
    return this.http.delete(this.APIUrl + '/employee/',val);
  }

  UploadPhoto(val:any){
    return this.http.post(this.APIUrl + '/SaveFile/',val);

  }

  getAllDepartmentNames():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/department/');
  }


}
