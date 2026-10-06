/* Infrastructure & Vehicle Partner form — client logic preserved verbatim, wrapped for this site. */
document.addEventListener("DOMContentLoaded",function(){
var districtsByState={
"Kerala":["Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode","Malappuram","Palakkad","Pathanamthitta","Thiruvananthapuram","Thrissur","Wayanad"],
"Tamil Nadu":["Ariyalur","Chengalpattu","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kallakurichi","Kancheepuram","Karur","Krishnagiri","Madurai","Mayiladuthurai","Nagapattinam","Kanniyakumari","Namakkal","Perambalur","Pudukkottai","Ramanathapuram","Ranipet","Salem","Sivaganga","Tenkasi","Thanjavur","Theni","Thoothukudi","Tiruchirappalli","Tirunelveli","Tirupathur","Tiruppur","Tiruvallur","Tiruvannamalai","Tiruvarur","Vellore","Viluppuram","Virudhunagar","The Nilgiris"],
"Karnataka":["Bagalkote","Ballari","Belagavi","Bengaluru Rural","Bengaluru Urban","Bidar","Chamarajanagara","Chikkaballapura","Chikkamagaluru","Chitradurga","Dakshina Kannada","Davanagere","Dharwad","Gadag","Hassan","Haveri","Kalaburagi","Kodagu","Kolar","Koppal","Mandya","Mysuru","Raichur","Ramanagara","Shivamogga","Tumakuru","Udupi","Uttara Kannada","Vijayanagara","Vijayapura","Yadgir"],
"Andhra Pradesh":["Alluri Sitharama Raju","Anakapalli","Anantapuramu","Annamayya","Bapatla","Chittoor","Dr. B. R. Ambedkar Konaseema","East Godavari","Eluru","Guntur","Kakinada","Krishna","Kurnool","Nandyal","NTR","Palnadu","Parvathipuram Manyam","Prakasam","Sri Potti Sriramulu Nellore","Sri Sathya Sai","Srikakulam","Tirupati","Visakhapatnam","Vizianagaram","West Godavari","YSR Kadapa"],
"Telangana":["Adilabad","Bhadradri Kothagudem","Hanumakonda","Hyderabad","Jagtial","Jangaon","Jayashankar Bhupalpally","Jogulamba Gadwal","Kamareddy","Karimnagar","Khammam","Kumuram Bheem Asifabad","Mahabubabad","Mahabubnagar","Mancherial","Medak","Medchal-Malkajgiri","Mulugu","Nagarkurnool","Nalgonda","Narayanpet","Nirmal","Nizamabad","Peddapalli","Rajanna Sircilla","Rangareddy","Sangareddy","Siddipet","Suryapet","Vikarabad","Wanaparthy","Warangal","Yadadri Bhuvanagiri"],
"Maharashtra":["Ahmednagar","Akola","Amravati","Aurangabad","Beed","Bhandara","Buldhana","Chandrapur","Dhule","Gadchiroli","Gondia","Hingoli","Jalgaon","Jalna","Kolhapur","Latur","Mumbai City","Mumbai Suburban","Nagpur","Nanded","Nandurbar","Nashik","Osmanabad","Palghar","Parbhani","Pune","Raigad","Ratnagiri","Sangli","Satara","Sindhudurg","Solapur","Thane","Wardha","Washim","Yavatmal"]};
var stateSelect=document.getElementById("spState"),districtSelect=document.getElementById("spDistrict"),offeringSelect=document.getElementById("spOffering"),existingWarehouseSection=document.getElementById("existingWarehouseSection"),buildWarehouseSection=document.getElementById("buildWarehouseSection"),vehicleSection=document.getElementById("vehicleSection"),form=document.getElementById("spInfraForm");
stateSelect.addEventListener("change",function(){var s=stateSelect.value;districtSelect.innerHTML='<option value="">Select District</option>';if(!s||!districtsByState[s]){districtSelect.disabled=true;return;}districtsByState[s].forEach(function(d){var o=document.createElement("option");o.value=d;o.textContent=d;districtSelect.appendChild(o);});districtSelect.disabled=false;});
offeringSelect.addEventListener("change",function(){hideAllConditionalSections();setSectionRequired(existingWarehouseSection,false);setSectionRequired(buildWarehouseSection,false);setSectionRequired(vehicleSection,false);if(offeringSelect.value==="Existing Warehouse on Lease"){existingWarehouseSection.style.display="block";setSectionRequired(existingWarehouseSection,true);}else if(offeringSelect.value==="Build and Lease Warehouse"){buildWarehouseSection.style.display="block";setSectionRequired(buildWarehouseSection,true);}else if(offeringSelect.value==="Vehicle Support"){vehicleSection.style.display="block";setSectionRequired(vehicleSection,true);}});
function hideAllConditionalSections(){existingWarehouseSection.style.display="none";buildWarehouseSection.style.display="none";vehicleSection.style.display="none";}
function setSectionRequired(section,requiredStatus){var fields=section.querySelectorAll("[data-required='true']");fields.forEach(function(field){field.required=requiredStatus;});}

/* ---- Source Pro site enhancements (the client logic above is unchanged) ---- */
var submitBtn=form.querySelector(".sp-submit-btn");
var statusBox=document.getElementById("spStatus");
var PLACEHOLDER_ACTION="/infrastructure-partner-submit/";
submitBtn.insertAdjacentHTML("afterbegin",'<span class="spinner" aria-hidden="true"></span>');

function visibleFields(){return Array.prototype.filter.call(form.querySelectorAll("input,select,textarea"),function(f){return f.type!=="submit"&&!f.disabled&&f.offsetParent!==null;});}
function fieldWrap(f){return f.closest(".sp-field")||f.closest(".sp-consent");}
function labelText(f){var l=form.querySelector('label[for="'+f.id+'"]');return l?l.textContent.replace("*","").trim():"This field";}
function setError(f,msg){
  var w=fieldWrap(f);if(!w)return;
  var err=w.querySelector(".sp-error");
  if(!err){err=document.createElement("p");err.className="sp-error";err.id=(f.id||f.name)+"-err";err.setAttribute("role","alert");w.appendChild(err);}
  if(msg){w.classList.add("has-error");err.textContent=msg;f.setAttribute("aria-invalid","true");f.setAttribute("aria-describedby",err.id);}
  else{w.classList.remove("has-error");err.textContent="";f.removeAttribute("aria-invalid");f.removeAttribute("aria-describedby");}
}
function validate(f){
  if(f.checkValidity()){setError(f,"");return true;}
  var v=f.validity,m="Please check this field.";
  if(v.valueMissing)m=f.type==="checkbox"?"Please confirm to continue.":(f.tagName==="SELECT"?"Please select an option.":"This field is required.");
  else if(v.typeMismatch)m=f.type==="email"?"Enter a valid email address.":"Enter a valid link, starting with https://";
  else if(v.rangeUnderflow||v.rangeOverflow)m="Enter a value between "+(f.min||"0")+(f.max?" and "+f.max:" or more")+".";
  setError(f,m);return false;
}
form.addEventListener("blur",function(e){var f=e.target;if(f.matches&&f.matches("input,select,textarea")&&f.type!=="file"&&(f.value||f.required))validate(f);},true);
form.addEventListener("input",function(e){var w=fieldWrap(e.target);if(w&&w.classList.contains("has-error"))validate(e.target);});
form.addEventListener("change",function(e){var w=fieldWrap(e.target);if(w&&w.classList.contains("has-error"))validate(e.target);});

function showStatus(kind,html){statusBox.className="sp-status sp-status--"+kind+" is-visible";statusBox.innerHTML=html;statusBox.focus();}

form.setAttribute("novalidate","novalidate");
form.addEventListener("submit",function(event){
  var bad=visibleFields().filter(function(f){return !validate(f);});
  if(bad.length){
    event.preventDefault();
    showStatus("error","<strong>Please fix "+bad.length+" field"+(bad.length>1?"s":"")+" before submitting:</strong><ul>"+bad.map(function(f){return "<li>"+labelText(f)+"</li>";}).join("")+"</ul>");
    bad[0].focus();return;
  }
  /* client logic: placeholder endpoint is not connected yet */
  if(form.getAttribute("action")===PLACEHOLDER_ACTION){
    event.preventDefault();
    showStatus("info","<strong>Form layout is ready.</strong> Please connect this form to your WordPress form handler, CRM, webhook, or backend submission URL before going live.");
    return;
  }
  submitBtn.setAttribute("aria-busy","true");submitBtn.disabled=false;
  submitBtn.lastChild.textContent="Submitting…";
});
window.addEventListener("pageshow",function(){submitBtn.removeAttribute("aria-busy");});
/* success state: have the backend redirect back with #submitted */
if(location.hash==="#submitted"){showStatus("success","<strong>Thank you.</strong> Your partnership interest has been received. The Source Pro team may contact you for verification and partnership discussions.");}

});
