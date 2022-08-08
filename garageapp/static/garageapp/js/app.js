const colorcode=document.getElementById('id_vehicle_form-color')
const colorname =document.getElementById('id_vehicle_form-colorname')
const variantcode=document.getElementById('id_vehicle_form-vehiclevariant')
const variantname=document.getElementById('id_vehicle_form-vehiclevariantname')
const modelcode=document.getElementById('id_vehicle_form-vehiclemodel')
const modelname=document.getElementById('id_vehicle_form-vehiclemodelname')
const servicecode=document.getElementById("id_vehicle_form-servicetype")
const servicename=document.getElementById("id_vehicle_form-servicetypename")
const isServiceadv=document.getElementById("id_vehicle_form-service_advisor")
const serviceadvname=document.getElementById("id_vehicle_form-service_advisorname")
const isTech=document.getElementById("id_vehicle_form-technician")
const techname=document.getElementById("id_vehicle_form-technicianname")
const isTechadv=document.getElementById("id_vehicle_form-technical_advisor")
const techadvname=document.getElementById("id_vehicle_form-technical_advisorname")
const jobcardno=document.getElementById("id_jobcard_form-jobcardno")
const regno=document.getElementById("id_vehicle_form-regno")
const omr=document.getElementById("id_vehicle_form-omr")
const washtype=document.getElementById("id_vehicle_form-washtype")
const chasisno=document.getElementById("id_vehicle_form-chasisno")
const custname=document.getElementById("id_customer_form-customername")
const custaddress=document.getElementById("id_customer_form-customeraddress")
const city=document.getElementById("id_customer_form-city")
const state=document.getElementById("id_customer_form-state")
const email=document.getElementById("id_customer_form-email")
const phone=document.getElementById("id_customer_form-phone")
const mobile=document.getElementById("id_customer_form-mobile")
const gst=document.getElementById("id_customer_form-gstin")
const pan=document.getElementById("id_customer_form-pan")
const osamount=document.getElementById("id_customer_form-outstanding_amt")

const demandcodelist = document.querySelectorAll('.Demandform_Demandcode')
//const demformdemandcode=document.getElementsByClassName("Demandform_Demandcode")
const demformdemanddesc=document.getElementById("demandform_demanddesc")

const labourcodelist=document.querySelectorAll('.lbspecial')
const labourdescription=document.getElementById('labourdescription')
const totalamt=document.getElementById('totalamount')
const labouramountlist=document.querySelectorAll('.lbamtspecial')
//const labouramount=document.getElementById('id_form-0-labouramt')
const itemcodelist=document.querySelectorAll('.classitemcode')
const itemdesclist=document.querySelectorAll('.classitemdesc')

const billqty=document.getElementById("billqtyid")
const listpartnocntrl=document.querySelectorAll(".partnoclass")
const reqlist=document.querySelectorAll('.reqclass')
const issuedlist=document.querySelectorAll('.issuedclass')
const issuelist=document.querySelectorAll('.issueclass')
const partno=document.getElementById('partnoctrl')
const batchctrl=document.getElementById('batchcntrl')


const getBatchCode=async (e)=>{
  const partscodeview=e.target.value
  console.log(partscodeview)
  const response = await fetch(`http://localhost:8000/getBatchcode/${partscodeview}`)
  const body=await response.json()
  console.log(body)
  batchctrl.innerHTML=""
  body.forEach(function(profile, index, myArray) {
    console.log(`Index: ${index}, Name: ${profile.batchcode}`);
    var opt = document.createElement('option');
    opt.value = index;
    opt.innerHTML = profile.batchcode;
    batchctrl.appendChild(opt)
});

}
if(partno){
  partno.addEventListener('change',getBatchCode)
}
//const requestedqty=document.getElementById("id_form-0-requestedqty")
const getPartsValues=async (e)=>{
  const amount=e.target.value
  console.log(amount)
  const reqamountid=e.target.id
  const partnocombo = document.querySelectorAll("[name$=partno]");
  const arrlist = Array.from(partnocombo)
  const found = arrlist.find(element => element.options[element.selectedIndex].text=='---------');
  console.log(found)
  const partnoselectedtext = partno.options[partno.selectedIndex].text;
  const foundsameitem = arrlist.find(element => element.options[element.selectedIndex].text===partnoselectedtext);
  if (foundsameitem === undefined){
  for (var i = 0; i < found.options.length; i++) {
    if (found.options[i].text === partnoselectedtext) {
        found.selectedIndex = i;
        break;
    }
  }
 }
 else{
  alert("Part already added")
 }
foundid = found.id
const indexarray=foundid.split("-")
const req_qtyid=`id_form-${indexarray[1]}-requestedqty`
const ctrlreq_qty=document.getElementById(`${req_qtyid}`)
ctrlreq_qty.value = amount

const issuedqtyid=`id_form-${indexarray[1]}-issuedqty`
const ctrlissuedqty=document.getElementById(`${issuedqtyid}`)
ctrlissuedqty.value = amount

const issueqtyid=`id_form-${indexarray[1]}-issueqty`
const ctrlissueqty=document.getElementById(`${issueqtyid}`)
ctrlissueqty.value = amount

const totalissueamt=document.getElementById("totalissueqty")
const amountarray = Array.from(issuelist)

var totalamount= amountarray.reduce(myFunc,0);
console.log(totalamount)
totalissueamt.value = totalamount

}
function myFunc(total, num) {
  
  return total + Number(num.value);
}
if(billqty){
  billqty.addEventListener('change',getPartsValues)
}


const checkDuplicatePart=async (e)=>{
  ///alert("Part ALert")
  const partcode=e.target.value
  const partid=e.target.id 
  //const labourftext=e.options[e.selectedIndex].text
  for (let item of listpartnocntrl){
    let parttest=item.options[item.selectedIndex].value
    
    if(partid!=item.id){
    //console.log(labourftext)
    console.log(parttest)
    if (partcode===parttest){
      alert("Part already exists")
      e.target.focus
      e.target.value=""
      break
    }
  }
   
  }
}

if(listpartnocntrl){
  for (let item of listpartnocntrl){
    item.addEventListener('change',checkDuplicatePart)
  }
}
//e is the global object passed to a function which handles any event of any controls
//this has a property called target and that property represents the control itself.
//so if we say e.target.id then w will get back the id of that particular control which invoked the event
const getCombovalues=async (e)=>{
  //form-0-itemdesc form-0-itemcode
  //id_form-0-itemcode
  const itemcode=e.target.id
  const myarray=itemcode.split("-")
  const itemdesc=`id_form-${myarray[1]}-itemdesc`
  const ctrlitemdesc=document.getElementById(`${itemdesc}`)
  ctrlitemdesc.value='desc' + e.target.value
  console.log(ctrlitemdesc)
}

if(itemcodelist){
  for (let item of itemcodelist){
  item.addEventListener('change',getCombovalues)
}
}

const checkDuplicateLabour=async (e)=>{
  const labourcode=e.target.value
  const labourid=e.target.id 
  //const labourftext=e.options[e.selectedIndex].text
  for (let item of labourcodelist){
    let labourtest=item.options[item.selectedIndex].value
    
    if(labourid!=item.id){
    //console.log(labourftext)
    console.log(labourtest)
    if (labourcode===labourtest){
      alert("Labour already exists")
      e.target.focus
      e.target.value=""
      break
    }
  }
   
  }
}

if(labourcodelist){
  for (let item of labourcodelist){
    item.addEventListener('change',checkDuplicateLabour)
  }
}
 



const getLabourdescription=async (e)=>{
  
  const labourcodeview=e.target.value
  const response = await fetch(`http://localhost:8000/getLabourdescription/${labourcodeview}`)
  const body = await response.json()
  //console.log(body[0].labourdescription)
  if (body.length>0){
    labourdescription.value=body[0].labourdesc
  }
}
if(labourcodelist){
  for (let item of labourcodelist){
    item.addEventListener('change',getLabourdescription)
  }
}

const getLabouramount=async (e)=>{
  //alert("Hii")
  const labourcodeview=e.target.value
  console.log(labourcodeview)
  const labourcode=e.target.id
  const indexarray=labourcode.split("-")
  const labouramt=`id_form-${indexarray[1]}-labouramt`
  const ctrllabouramt=document.getElementById(`${labouramt}`)
  const response = await fetch(`http://localhost:8000/getLabouramount/${labourcodeview}`)
  const body = await response.json()
  if (body.length>0){
    ctrllabouramt.value=body[0].labouramount
  }
  let total=0
  
  for (let i=0; i<labouramountlist.length; i++){
    //total=total+getLabouramount(
    console.log(typeof(labouramountlist[i].value))
    if(labouramountlist[i].value===""){
    }
    else{
      total=parseInt(total)+parseInt(labouramountlist[i].value)
      totalamt.value=total 
    }
  }
}
if(labourcodelist){
  for (let item of labourcodelist){
    item.addEventListener('change',getLabouramount)
  }
}

const getTotalLabouramt=async (e)=>{
  
  // let total=0
  
  // for (let i=0; i<labouramountlist.length; i++){
  //   //total=total+getLabouramount(
  //   console.log(typeof(labouramountlist[i].value))
  //   if(labouramountlist[i].value===""){
  //   }
  //   else{
  //     total=parseInt(total)+parseInt(labouramountlist[i].value)
  //     totalamt.value=total 
  //   }
  // }
  
 
}
if(labourcodelist){
  //alert("HIIII")
  for (var i = 0; i < labourcodelist.length; i++) {
    
    labourcodelist[i].addEventListener('change',getTotalLabouramt);
}
}
const getDemanddescription=async (e)=>{
  alert("HIIII")
  const demandcodeview=e.target.value
  const response = await fetch(`http://localhost:8000/getDemanddescription/${demandcodeview}`)
  const body = await response.json()
  console.log(body[0].demformdemanddesc)
  if (body.length>0){
    demformdemanddesc.value=body[0].demand_desc
  }
}

if(demandcodelist){
  for (let item of demandcodelist) {
    
    item.addEventListener('change',getDemanddescription)
  }
  
}

const getcolorname=async (e)=>{
  alert('jiiii')
  const colorcodeview=e.target.value
  
    const response = await fetch(`http://localhost:8000/getcolorname/${colorcodeview}`)
    const body = await response.json()
    console.log(body[0].colorname)
    if (body.length>0){
      alert("Class name already exists")
      colorname.value=body[0].colorname
    }
}

if(colorcode){
  colorcode.addEventListener('change',getcolorname)
}

const getvariantname=async (e)=>{
  alert('jiiii')
  const variantcodeview=e.target.value
  
    const response = await fetch(`http://localhost:8000/getvariantname/${variantcodeview}`)
    const body = await response.json()
    console.log(body[0].variantname)
    if (body.length>0){
      alert("Variant name exists")
      variantname.value=body[0].variantname
    }
}
if(variantcode){
  variantcode.addEventListener('change',getvariantname)
}

const getmodelname=async (e)=>{
  alert('jiiii')
  const modelcodeview=e.target.value
  
    const response = await fetch(`http://localhost:8000/getmodelname/${modelcodeview}`)
    const body = await response.json()
    console.log(body[0].modelname)
    if (body.length>0){
      alert("Model name exists")
      modelname.value=body[0].modelname
    }
}
if(modelcode){
  modelcode.addEventListener('change',getmodelname)
}

const getservicename=async (e)=>{
  alert('jiiii')
  const servicecodeview=e.target.value
  
    const response = await fetch(`http://localhost:8000/getservicename/${servicecodeview}`)
    const body = await response.json()
    console.log(body[0].servicename)
    if (body.length>0){
      alert("Service name exists")
      servicename.value=body[0].servicename
    }
}
if(servicecode){
  servicecode.addEventListener('change',getservicename)
}

const getserviceadvisor=async (e)=>{
  alert('jiiii')
  const serviceadvisorcodeview=e.target.value
  
    const response = await fetch(`http://localhost:8000/getserviceadvisor/${serviceadvisorcodeview}`)
    const body = await response.json()
    console.log(body[0].name)
    if (body.length>0){
      alert("Name exists")
      serviceadvname.value=body[0].name
    }
}
if(isServiceadv){
  isServiceadv.addEventListener('change',getserviceadvisor)
}

const gettechnician=async (e)=>{
  alert('jiiii')
  const technicianview=e.target.value
  
    const response = await fetch(`http://localhost:8000/gettechnician/${technicianview}`)
    const body = await response.json()
    console.log(body[0].name)
    if (body.length>0){
      alert("Name exists")
      techname.value=body[0].name
    }
}
if(isTech){
  isTech.addEventListener('change',gettechnician)
}

const gettechnicaladvisor=async (e)=>{

  const technicaladvisorcodeview=e.target.value
  
    const response = await fetch(`http://localhost:8000/gettechnicaladvisor/${technicaladvisorcodeview}`)
    const body = await response.json()
    console.log(body[0].name)
    if (body.length>0){
     
      techadvname.value=body[0].name
    }
}
if(isTechadv){
  isTechadv.addEventListener('change',gettechnicaladvisor)
}

const getJobcardDetails=async (e)=>{
  alert('hiiii')
  const jobcardno=e.target.value
  
    const response = await fetch(`http://localhost:8000/getJobcardDetails/${jobcardno}`)
    const body = await response.json()
    console.log(body[3].colorname)
    //jobcardinstance
    var datandtime=document.getElementById('id_jobcard_form-datetime') 
    datandtime.value=body[0].datetime
    var checkindt=document.getElementById('id_jobcard_form-checkindatetime')
    checkindt.value=body[0].checkindatetime
    //vehicleinstance
    regno.value=body[1].regno
    omr.value=body[1].omr
    //Service type code and servicename(using views.py chain method)
    servicecode.value=body[1].servicetype
    servicename.value=body[4].servicename
    washtype.value=body[1].washtype
    //Service advisor code and name
    isServiceadv.value=body[1].service_advisor
    var serviceadvisorcodeview=isServiceadv.value
    var serviceadvisorname=await fetch(`http://localhost:8000/getserviceadvisor/${serviceadvisorcodeview}`)
    var serviceadvnamejson=await serviceadvisorname.json()
    console.log(serviceadvnamejson[0].name)
    serviceadvname.value=serviceadvnamejson[0].name
    //Technician code and technician name
    isTech.value=body[1].technician
    var technicianview=isTech.value
    var technicianname=await fetch(`http://localhost:8000/gettechnician/${technicianview}`)
    var techniciannamejson=await technicianname.json()
    console.log(techniciannamejson[0].name)
    techname.value=techniciannamejson[0].name
    //Technical advisor code and name
    isTechadv.value=body[1].technical_advisor
    var technicaladvisorcodeview= isTechadv.value
    var technicadvame=await fetch(`http://localhost:8000/gettechnicaladvisor/${technicaladvisorcodeview}`)
    var technamejson=await technicadvame.json()
    console.log(technamejson[0].name)
    techadvname.value=technamejson[0].name
    //Vehicle model code and model name
    modelcode.value=body[1].vehiclemodel
    var modelcodeview=modelcode.value
    var vehiclemodelname=await fetch(`http://localhost:8000/getmodelname/${modelcodeview}`)
    var modelnamejson=await vehiclemodelname.json()
    console.log(modelnamejson[0].modelname)
    modelname.value=modelnamejson[0].modelname
    chasisno.value=body[1].chasisno
    //Variant code and name (through views.py chain method)
    variantcode.value=body[1].vehiclevariant
    variantname.value=body[5].variantname
    //Color code and colorname (through views.py code chain method)
    colorcode.value=body[1].color
    colorname.value=body[3].colorname
    //customerinstance
    custname.value=body[2].customername
    custaddress.value=body[2].customeraddress
    city.value=body[2].city
    state.value=body[2].state
    email.value=body[2].email
    phone.value=body[2].phone
    mobile.value=body[2].mobile
    gst.value=body[2].gstin
    pan.value=body[2].pan
    osamount.value=body[2].outstanding_amt


}
if(jobcardno){
  jobcardno.addEventListener('change',getJobcardDetails)
}


















// function CompareMinMaxage()
// {
// const minage=document.getElementById('id_classminage')
// const maxage=document.getElementById('id_classmaxage')
// if (Number(minage.value)>Number(maxage.value)){
// alert("Minimum age should not exceed maximum age")
// }
// else{
//     alert("Values ok")
// }
// }
// if(classmaxage){
//   classmaxage.addEventListener('change',CompareMinMaxage)
// }

// const checkclassduplicate=async (e)=>{
    
//     const classnameval=e.target.value
    
//       const response = await fetch(`http://localhost:8000/isclassexists/${classnameval}`)
//       const body = await response.json()
//       console.log(body)
//       if (body.length>0){
//         alert("Class name already exists")
//         e.target.focus
//         e.target.value=""
//       }
// }
// //to check the range 
// const checkagerange=async (e)=>{
//   alert('hiiiii')
//     const classminageval=e.target.value
//     const maxage=classmaxage.value
//     if(classminageval>0 && maxage>0){
//     const response = await fetch(`http://localhost:8000/validateminage/${classminageval}/${maxage}`)
//     const body = await response.json()
//     console.log(body)
//     //if (){
//       if (body===false){
//       alert("Class range already exists, enter a valid range")
//       e.target.focus
//       e.target.value=""
//     }
//   }
//     //0-3,4-6,7-9,10-11,12-15 
//   }



 


