from flask import Flask,render_template,request,redirect,url_for
import os
import subprocess as sp

app = Flask(__name__, template_folder='../templates')
# if __name__ == "__main__":
#     app.run(debug=True, host="192.168.68.91", port=5000)


@app.route("/")
def index():
    #output = sp.getoutput('pytest -s -v testCases/EZWebDashboard/test_prf.py')
    #return output
    dr_iq_modules=['Manage User','User Management','Online Consultation-Order Medication',"Online Consultation-Women's Health and Contraception",
                   'Online Consultation-Urinary Tract Infection','Online Consultation-(Beta) Headache','Online Consultation-Joint or Muscular problems (Back Pain and Knee Pain)',
                   'Online Consultation-Request a Blood Test','Online Consultation-(Beta) General Medical Advice','Online Consultation-Administrative Help',
                   'Online Consultation-Mental Heath and Well-Being','Online Consultation-Skin Problem','Online Consultation-Coronavirus',
                   'Online Consultation-Enter Health Data','Online Consultation-Request General Advice','Online Consultation-(Beta) Quick Query',
                   'Online Consultation-Medication Query/Problem','Online Consultation-Request a Medical Certificate','Online Consultation-Template Pathway',
                   'Online Consultation Configuration', 'Appointments', 'Appointment Confuguration', 'Medication', 'Patient Profile Update', 'Practice Change Requests',
                   'Out of Office', 'Account Removal requests', 'GP Connect', 'Self Help Advice', 'Registration of Existing user,New user and PDs user',
                   'My Medical Record', 'Covid Vacccination Certificate', 'System One user', 'By Directional Messages (BDM)-Start Conversation',
                   'By Directional Messages (BDM)-Message Count in APP', 'By Directional Messages (BDM)-Unread Messages', 'By Directional Messages (BDM)-Filter',
                   'By Directional Messages (BDM)-Closed Conversation', 'By Directional Messages (BDM)-Closed Conversation Notification',
                   'By Directional Messages (BDM)-Images in Conversation', 'By Directional Messages (BDM)-Attachment in Conversation',
                   'By Directional Messages (BDM)-Links in Coversation','By Directional Messages (BDM)-Subject Mandatory','By Directional Messages (BDM)-Practice Filter',
                   'By Directional Messages (BDM)-Search Name', 'By Directional Messages (BDM)-Download PDF', 'By Directional Messages (BDM)-Copy Summary',
                   'By Directional Messages (BDM)-Closed Conversation Date/Time Stamp in Dashboard and App','Practice Profile Update (web)',
                   'Count Verification from left bar (web)', 'Practice Change Password (web)', 'Patient Change password (app)','Add Personal Detail (app)',
                   'Feedback (app)']
    ez_web_modules=['Patient Registration Form','Travel Risk Form','PPG Joiner Form','Complaint Form','Feedback Form','Medical Certificate Fees Form',
                    'Medical Certificate No Fees Form','Friends and Family Survey Form','Repeat Prescription Request','Prescription Question',
                    'Prescription Synchronization','Medication Review','Electronic Prescription Form','Change Personal Details']
    return render_template('test.html',dr_iq_modules=dr_iq_modules,ez_web_modules=ez_web_modules)

@app.route("/saveForm", methods=['GET','POST'])
def saveForm():
    #output = sp.getoutput('pytest -s -v testCases/EZWebDashboard/test_prf.py')
    selectedModuleDrIq=None
    selectedModuleEzWeb=None
    selectedModule=None

    if request.method== "POST":
        #Purchase Item Logic
        selectedProject = request.form.get('project_name')
        selectedcycle   = request.form.get('testingcycle')
        selectedModuleDrIq = request.form.get('selectedmodule_driq')
        selectedModuleEzWeb = request.form.get('selectedmodule_ezweb')
        if selectedModuleDrIq == '0' :
            selectedModule= selectedModuleEzWeb
        else:
            selectedModule= selectedModuleDrIq

        if selectedcycle == 'smoke':
    ############################ DR IQ Modules #######################################################
            if selectedModule == 'Manage User':
                return 'pass smoke test url for Manage User Form in DR IQ'
            elif selectedModule == 'User Management':
                return 'pass smoke test url for User Management Form in DR IQ'
            elif selectedModule == 'Online Consultation-Order Medication':
                return 'pass smoke test url for Online Consultation-Order Medication in DR IQ'
            elif selectedModule == "Online Consultation-Women's Health and Contraception":
                return "pass smoke test url for Online Consultation-Women's Health and Contraception in DR IQ"
            elif selectedModule == "Online Consultation-Urinary Tract Infection":
                return "pass smoke test url for Online Consultation-Urinary Tract Infection in DR IQ"
            elif selectedModule == "Online Consultation-(Beta) Headache":
                return "pass smoke test url for Online Consultation-(Beta) Headache in DR IQ"
            elif selectedModule == "Online Consultation-Joint or Muscular problems (Back Pain and Knee Pain)":
                return "pass smoke test url for Online Consultation-Joint or Muscular problems (Back Pain and Knee Pain) in DR IQ"
            elif selectedModule == "Online Consultation-Request a Blood Test":
                return "pass smoke test url for Online Consultation-Request a Blood Test in DR IQ"
            elif selectedModule == "Online Consultation-(Beta) General Medical Advice":
                return "pass smoke test url for Online Consultation-(Beta) General Medical Advice in DR IQ"
            elif selectedModule == "Online Consultation-Administrative Help":
                return "pass smoke test url for Online Consultation-Administrative Help in DR IQ"
            elif selectedModule == "Online Consultation-Mental Heath and Well-Being":
                return "pass smoke test url for Online Consultation-Mental Heath and Well-Being in DR IQ"
            elif selectedModule == "Online Consultation-Skin Problem":
                return "pass smoke test url for Online Consultation-Skin Problem in DR IQ"
            elif selectedModule == "Online Consultation-Coronavirus":
                return "pass smoke test url for Online Consultation-Coronavirus in DR IQ"
            elif selectedModule == "Online Consultation-Enter Health Data":
                return "pass smoke test url for Online Consultation-Enter Health Data in DR IQ"
            elif selectedModule == "Online Consultation-Request General Advice":
                return "pass smoke test url for Online Consultation-Request General Advice in DR IQ"
            elif selectedModule == "Online Consultation-(Beta) Quick Query":
                return "pass smoke test url for Online Consultation-(Beta) Quick Query in DR IQ"
            elif selectedModule == "Online Consultation-Medication Query/Problem":
                return "pass smoke test url for Online Consultation-Medication Query/Problem in DR IQ"
            elif selectedModule == "Online Consultation-Request a Medical Certificate":
                return "pass smoke test url for Online Consultation-Request a Medical Certificate in DR IQ"
            elif selectedModule == "Online Consultation-Template Pathway":
                return "pass smoke test url for Online Consultation-Template Pathway in DR IQ"
            elif selectedModule == 'Online Consultation Configuration':
                return 'pass smoke test url for Online Consultation Configuration in DR IQ'
            elif selectedModule == 'Appointments':
                return 'pass smoke test url for Appointments in DR IQ'
            elif selectedModule == 'Appointment Confuguration':
                return 'pass smoke test url for Appointment Confuguration in DR IQ'
            elif selectedModule == 'Medication':
                return 'pass smoke test url for Medication in DR IQ'
            elif selectedModule == 'Patient Profile Update':
                return 'pass smoke test url for Patient Profile Update in DR IQ'
            elif selectedModule == 'Practice Change Requests':
                return 'pass smoke test url for Practice Change Requests in DR IQ'
            elif selectedModule == 'Out of Office':
                return 'pass smoke test url for Out of Office  in DR IQ'
            elif selectedModule == 'Account Removal requests':
                return 'pass smoke test url for Account Removal requests  in DR IQ'
            elif selectedModule == 'GP Connect':
                return 'pass smoke test url for GP Connect in DR IQ'
            elif selectedModule == 'Self Help Advice':
                return 'pass smoke test url for Self Help Advice in DR IQ'
            elif selectedModule == 'Registration of Existing user,New user and PDs user':
                return 'pass smoke test url for Registration of Existing user,New user and PDs user in DR IQ'
            elif selectedModule == 'My Medical Record':
                return 'pass smoke test url for My Medical Record in DR IQ'
            elif selectedModule == 'Covid Vacccination Certificate':
                return 'pass smoke test url for Covid Vacccination Certificate in DR IQ'
            elif selectedModule == 'System One user':
                return 'pass smoke test url for System One user in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Start Conversation':
                return 'pass smoke test url for By Directional Messages (BDM)-Start Conversation in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Message Count in APP':
                return 'pass smoke test url for By Directional Messages (BDM)-Message Count in APP in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Unread Messages':
                return 'pass smoke test url for By Directional Messages (BDM)-Unread Messages in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Filter':
                return 'pass smoke test url for By Directional Messages (BDM)-Filter in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Closed Conversation':
                return 'pass smoke test url for By Directional Messages (BDM)-Closed Conversation in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Closed Conversation Notification':
                return 'pass smoke test url for By Directional Messages (BDM)-Closed Conversation Notification in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Images in Conversation':
                return 'pass smoke test url for By Directional Messages (BDM)-Images in Conversation in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Attachment in Conversation':
                return 'pass smoke test url for By Directional Messages (BDM)-Attachment in Conversation in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Links in Coversation':
                return 'pass smoke test url for By Directional Messages (BDM)-Links in Coversation in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Subject Mandatory':
                return 'pass smoke test url for By Directional Messages (BDM)-Subject Mandatory in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Practice Filter':
                return 'pass smoke test url for By Directional Messages (BDM)-Practice Filter in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Search Name':
                return 'pass smoke test url for By Directional Messages (BDM)-Search Name in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Download PDF':
                return 'pass smoke test url for By Directional Messages (BDM)-Download PDF in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Copy Summary':
                return 'pass smoke test url for By Directional Messages (BDM)-Copy Summary in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Closed Conversation Date/Time Stamp in Dashboard and App':
                return 'pass smoke test url for By Directional Messages (BDM)-Closed Conversation Date/Time Stamp in Dashboard and App in DR IQ'
            elif selectedModule == 'Practice Profile Update (web)':
                return 'pass smoke test url for Practice Profile Update (web) in DR IQ'
            elif selectedModule == 'Count Verification from left bar (web)':
                return 'pass smoke test url for Count Verification from left bar (web) in DR IQ'
            elif selectedModule == 'Practice Change Password (web)':
                return 'pass smoke test url for Practice Change Password (web) in DR IQ'
            elif selectedModule == 'Patient Change password (app)':
                return 'pass smoke test url for Patient Change password (app) in DR IQ'
            elif selectedModule == 'Add Personal Detail (app)':
                return 'pass smoke test url for Add Personal Detail (app) in DR IQ'
            elif selectedModule == 'Feedback (app)':
                return 'pass smoke test url for Feedback (app) in DR IQ'
   ################################################## EZ WEB MODULES ###############################################
            elif selectedModule == 'Patient Registration Form':
                output = sp.getoutput('pytest -s -v --alluredir="C:\\Users\\DELL\\PycharmProjects\\pythonFramework\\Reports" testCases/EZWebDashboard/test_prf.py')
                #os.system('pytest -s -v testCases/EZWebDashboard/test_prf.py')
                return 'pass smoke test url for Patient Registration Form in EZWEB'
            elif selectedModule == 'Travel Risk Form':
                return 'pass smoke test url for Travel Risk Form in EZWEB'
            elif selectedModule == 'PPG Joiner Form':
                return 'pass smoke test url for PPG Joiner Form in EZWEB'
            elif selectedModule == 'Complaint Form':
                return 'pass smoke test url for Complaint Form Form in EZWEB'
            elif selectedModule == 'Feedback Form':
                return 'pass smoke test url for Feedback Form in EZWEB'
            elif selectedModule == 'Medical Certificate Fees Form':
                return 'pass smoke test url for Medical Certificate Fees Form in EZWEB'
            elif selectedModule == 'Medical Certificate No Fees Form':
                return 'pass smoke test url for Medical Certificate No Fees Form in EZWEB'
            elif selectedModule == 'Friends and Family Survey Form':
                return 'pass smoke test url for Friends and Family Survey Form in EZWEB'
            elif selectedModule == 'Repeat Prescription Request':
                return 'pass smoke test url for Repeat Prescription Request Form in EZWEB'
            elif selectedModule == 'Prescription Question':
                return 'pass smoke test url for Prescription Question Form in EZWEB'
            elif selectedModule == 'Prescription Synchronization':
                return 'pass smoke test url for Prescription Synchronization Form in EZWEB'
            elif selectedModule == 'Medication Review':
                return 'pass smoke test url for Medication Review Form in EZWEB'
            elif selectedModule == 'Electronic Prescription Form':
                return 'pass smoke test url for Electronic Prescription Form in EZWEB'
            elif selectedModule == 'Change Personal Details':
                return 'pass smoke test url for Change Personal Details Form in EZWEB'


        else:
            ############################ DR IQ Modules #######################################################
            if selectedModule == 'Manage User':
                return 'pass regression test url for Manage User Form in DR IQ'
            elif selectedModule == 'User Management':
                return 'pass regression test url for User Management Form in DR IQ'
            elif selectedModule == 'Online Consultation-Order Medication':
                return 'pass regression test url for Online Consultation-Order Medication in DR IQ'
            elif selectedModule == "Online Consultation-Women's Health and Contraception":
                return "pass regression test url for Online Consultation-Women's Health and Contraception in DR IQ"
            elif selectedModule == "Online Consultation-Urinary Tract Infection":
                return "pass regression test url for Online Consultation-Urinary Tract Infection in DR IQ"
            elif selectedModule == "Online Consultation-(Beta) Headache":
                return "pass regression test url for Online Consultation-(Beta) Headache in DR IQ"
            elif selectedModule == "Online Consultation-Joint or Muscular problems (Back Pain and Knee Pain)":
                return "pass regression test url for Online Consultation-Joint or Muscular problems (Back Pain and Knee Pain) in DR IQ"
            elif selectedModule == "Online Consultation-Request a Blood Test":
                return "pass regression test url for Online Consultation-Request a Blood Test in DR IQ"
            elif selectedModule == "Online Consultation-(Beta) General Medical Advice":
                return "pass regression test url for Online Consultation-(Beta) General Medical Advice in DR IQ"
            elif selectedModule == "Online Consultation-Administrative Help":
                return "pass regression test url for Online Consultation-Administrative Help in DR IQ"
            elif selectedModule == "Online Consultation-Mental Heath and Well-Being":
                return "pass regression test url for Online Consultation-Mental Heath and Well-Being in DR IQ"
            elif selectedModule == "Online Consultation-Skin Problem":
                return "pass regression test url for Online Consultation-Skin Problem in DR IQ"
            elif selectedModule == "Online Consultation-Coronavirus":
                return "pass regression test url for Online Consultation-Coronavirus in DR IQ"
            elif selectedModule == "Online Consultation-Enter Health Data":
                return "pass regression test url for Online Consultation-Enter Health Data in DR IQ"
            elif selectedModule == "Online Consultation-Request General Advice":
                return "pass regression test url for Online Consultation-Request General Advice in DR IQ"
            elif selectedModule == "Online Consultation-(Beta) Quick Query":
                return "pass regression test url for Online Consultation-(Beta) Quick Query in DR IQ"
            elif selectedModule == "Online Consultation-Medication Query/Problem":
                return "pass regression test url for Online Consultation-Medication Query/Problem in DR IQ"
            elif selectedModule == "Online Consultation-Request a Medical Certificate":
                return "pass regression test url for Online Consultation-Request a Medical Certificate in DR IQ"
            elif selectedModule == "Online Consultation-Template Pathway":
                return "pass regression test url for Online Consultation-Template Pathway in DR IQ"
            elif selectedModule == 'Online Consultation Configuration':
                return 'pass regression test url for Online Consultation Configuration in DR IQ'
            elif selectedModule == 'Appointments':
                return 'pass regression test url for Appointments in DR IQ'
            elif selectedModule == 'Appointment Confuguration':
                return 'pass regression test url for Appointment Confuguration in DR IQ'
            elif selectedModule == 'Medication':
                return 'pass regression test url for Medication in DR IQ'
            elif selectedModule == 'Patient Profile Update':
                return 'pass regression test url for Patient Profile Update in DR IQ'
            elif selectedModule == 'Practice Change Requests':
                return 'pass regression test url for Practice Change Requests in DR IQ'
            elif selectedModule == 'Out of Office':
                return 'pass regression test url for Out of Office  in DR IQ'
            elif selectedModule == 'Account Removal requests':
                return 'pass regression test url for Account Removal requests  in DR IQ'
            elif selectedModule == 'GP Connect':
                return 'pass regression test url for GP Connect in DR IQ'
            elif selectedModule == 'Self Help Advice':
                return 'pass regression test url for Self Help Advice in DR IQ'
            elif selectedModule == 'Registration of Existing user,New user and PDs user':
                return 'pass regression test url for Registration of Existing user,New user and PDs user in DR IQ'
            elif selectedModule == 'My Medical Record':
                return 'pass regression test url for My Medical Record in DR IQ'
            elif selectedModule == 'Covid Vacccination Certificate':
                return 'pass regression test url for Covid Vacccination Certificate in DR IQ'
            elif selectedModule == 'System One user':
                return 'pass regression test url for System One user in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Start Conversation':
                return 'pass regression test url for By Directional Messages (BDM)-Start Conversation in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Message Count in APP':
                return 'pass regression test url for By Directional Messages (BDM)-Message Count in APP in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Unread Messages':
                return 'pass regression test url for By Directional Messages (BDM)-Unread Messages in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Filter':
                return 'pass regression test url for By Directional Messages (BDM)-Filter in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Closed Conversation':
                return 'pass regression test url for By Directional Messages (BDM)-Closed Conversation in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Closed Conversation Notification':
                return 'pass regression test url for By Directional Messages (BDM)-Closed Conversation Notification in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Images in Conversation':
                return 'pass regression test url for By Directional Messages (BDM)-Images in Conversation in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Attachment in Conversation':
                return 'pass regression test url for By Directional Messages (BDM)-Attachment in Conversation in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Links in Coversation':
                return 'pass regression test url for By Directional Messages (BDM)-Links in Coversation in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Subject Mandatory':
                return 'pass regression test url for By Directional Messages (BDM)-Subject Mandatory in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Practice Filter':
                return 'pass regression test url for By Directional Messages (BDM)-Practice Filter in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Search Name':
                return 'pass regression test url for By Directional Messages (BDM)-Search Name in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Download PDF':
                return 'pass regression test url for By Directional Messages (BDM)-Download PDF in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Copy Summary':
                return 'pass regression test url for By Directional Messages (BDM)-Copy Summary in DR IQ'
            elif selectedModule == 'By Directional Messages (BDM)-Closed Conversation Date/Time Stamp in Dashboard and App':
                return 'pass regression test url for By Directional Messages (BDM)-Closed Conversation Date/Time Stamp in Dashboard and App in DR IQ'
            elif selectedModule == 'Practice Profile Update (web)':
                return 'pass regression test url for Practice Profile Update (web) in DR IQ'
            elif selectedModule == 'Count Verification from left bar (web)':
                return 'pass regression test url for Count Verification from left bar (web) in DR IQ'
            elif selectedModule == 'Practice Change Password (web)':
                return 'pass regression test url for Practice Change Password (web) in DR IQ'
            elif selectedModule == 'Patient Change password (app)':
                return 'pass regression test url for Patient Change password (app) in DR IQ'
            elif selectedModule == 'Add Personal Detail (app)':
                return 'pass regression test url for Add Personal Detail (app) in DR IQ'
            elif selectedModule == 'Feedback (app)':
                return 'pass regression test url for Feedback (app) in DR IQ'
            ################################################## EZ WEB MODULES ###############################################
            elif selectedModule == 'Patient Registration Form':
                return 'pass regression test url for Patient Registration Form in EZWEB'
            elif selectedModule == 'Travel Risk Form':
                return 'pass regression test url for Travel Risk Form in EZWEB'
            elif selectedModule == 'PPG Joiner Form':
                return 'pass regression test url for PPG Joiner Form in EZWEB'
            elif selectedModule == 'Complaint Form':
                return 'pass regression test url for Complaint Form Form in EZWEB'
            elif selectedModule == 'Feedback Form':
                return 'pass regression test url for Feedback Form in EZWEB'
            elif selectedModule == 'Medical Certificate Fees Form':
                return 'pass regression test url for Medical Certificate Fees Form in EZWEB'
            elif selectedModule == 'Medical Certificate No Fees Form':
                return 'pass regression test url for Medical Certificate No Fees Form in EZWEB'
            elif selectedModule == 'Friends and Family Survey Form':
                return 'pass regression test url for Friends and Family Survey Form in EZWEB'
            elif selectedModule == 'Repeat Prescription Request':
                return 'pass regression test url for Repeat Prescription Request Form in EZWEB'
            elif selectedModule == 'Prescription Question':
                return 'pass regression test url for Prescription Question Form in EZWEB'
            elif selectedModule == 'Prescription Synchronization':
                return 'pass regression test url for Prescription Synchronization Form in EZWEB'
            elif selectedModule == 'Medication Review':
                return 'pass regression test url for Medication Review Form in EZWEB'
            elif selectedModule == 'Electronic Prescription Form':
                return 'pass regression test url for Electronic Prescription Form in EZWEB'
            elif selectedModule == 'Change Personal Details':
                return 'pass regression test url for Change Personal Details Form in EZWEB'



    else:
     return redirect(url_for('index'))









       