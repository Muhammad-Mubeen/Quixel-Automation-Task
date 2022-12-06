import pytest
from utilities.customlogger import LogGen
from pageObjects.Dr_iQ.pageObjects.App_GetStarted import AppGetStarted
from pageObjects.Dr_iQ.pageObjects.AppSignIn_CreateAccount import AppSignInCreateAccount
from pageObjects.Dr_iQ.pageObjects.DrIQ_Login import DrIQLogin
from pageObjects.Dr_iQ.pageObjects.App_UserGuide import AppUserGuide
from pageObjects.Dr_iQ.pageObjects.DrIQ_Home import DrIQHome
# from utilities.Next_Button import NextButton
# from utilities.No_Option import SelectNoOption
from pageObjects.Dr_iQ.pageObjects.Online_Consultation import OnlineConsultation
from pageObjects.Dr_iQ.pageObjects.Contraception import Contraception
from pageObjects.Dr_iQ.pageObjects.Order_Medication import ConsultationForMyself
from pageObjects.Dr_iQ.pageObjects.Contraception import SelectTheProblem
from pageObjects.Dr_iQ.pageObjects.Contraception import SelectPregnancy
from pageObjects.Dr_iQ.pageObjects.Contraception import MedicalConditions
from pageObjects.Dr_iQ.pageObjects.Contraception import SufferFromMigraines
from pageObjects.Dr_iQ.pageObjects.Contraception import SufferingFromAura
from pageObjects.Dr_iQ.pageObjects.Contraception import SchedulingOfAnyMajorSurgery
from pageObjects.Dr_iQ.pageObjects.Contraception import EnterInfo
from pageObjects.Dr_iQ.pageObjects.Contraception import ImmediateFamilyProblems
from pageObjects.Dr_iQ.pageObjects.Contraception import FamilyDiagnosisInfo
from pageObjects.Dr_iQ.pageObjects.Contraception import FamilyMemberHasCancers
from pageObjects.Dr_iQ.pageObjects.Contraception import SelectMedications
from pageObjects.Dr_iQ.pageObjects.Contraception import AllergiesToMedications
from pageObjects.Dr_iQ.pageObjects.Contraception import CurrentSmokingStatus
from pageObjects.Dr_iQ.pageObjects.Contraception import CigaretteQuantity
from pageObjects.Dr_iQ.pageObjects.Contraception import CalculateBMI
from pageObjects.Dr_iQ.pageObjects.Contraception import EnterCurrentPill
from pageObjects.Dr_iQ.pageObjects.Contraception import OtherInfo
from pageObjects.Dr_iQ.pageObjects.Order_Medication import SelectPharmacy
from pageObjects.Dr_iQ.pageObjects.Order_Medication import PharmacySearchByPostCode
from pageObjects.Dr_iQ.pageObjects.Order_Medication import EnterPreferredPharmacy
from pageObjects.Dr_iQ.pageObjects.Order_Medication import FinishPage
from pageObjects.Dr_iQ.pageObjects.Order_Medication import RequestConfirmationMenu
# from utilities.Back_Button import BackButton
from pageObjects.Dr_iQ.pageObjects.Contraception_PWD import DrIQPWDLogin
from pageObjects.Dr_iQ.pageObjects.Contraception_PWD import DrIQPWDHome
from pageObjects.Dr_iQ.pageObjects.Contraception_PWD import OnlineConsultationsListingPage
from pageObjects.Dr_iQ.pageObjects.Contraception_PWD import OnlineConsultationDetailPage
from pageObjects.Dr_iQ.pageObjects.Contraception_PWD import OutcomePopup


class TestContraceptionTC01:
    username = "aimantest@yopmail.com"
    password = "@Aiman@123"
    info = "Test"
    relationship = "Test"
    age = "34"
    diagnosis = "Test"
    bp_reading = "28.3"
    feet = "5"
    inch = "6"
    weight_in_kg = "65.5"
    pill = "test"
    other_info = "N/A"
    postcode = "SW21HT"
    baseURL = "https://qa-app.dr-iq.com/login"
    username_pwd = "Aiman.dashboard@yopmail.com"
    password_pwd = "Aiman@123"
    message = "test"
    pharmacy_details = "Greyfriars Pharmacy"

    # Calling and Initializing Logger Objects
    log = LogGen.loggen()

    @pytest.mark.sanity
    def test_contraception_mobile(self, setup1):
        self.driver = setup1
        self.driver.implicitly_wait(100)
        self.ags = AppGetStarted(self.driver)
        self.driver.implicitly_wait(100)
        self.log.info("******** Launching Application. Application is now on 'Get Started' screen ********")
        self.driver.implicitly_wait(100)
        self.ags.app_get_started()
        self.log.info("******** Clicking the app get started button ********")
        self.asi = AppSignInCreateAccount(self.driver)
        self.log.info("******** Application is now on 'Sign-in' or 'Create account' screen ********")
        self.asi.app_sign_in()
        self.log.info("******** Clicking 'sign in' button ********")
        self.lp = DrIQLogin(self.driver)
        self.log.info("******** Application is now on 'Welcome to Dr.iQ. Please Sign in' screen ********")
        self.lp.set_username(self.username)
        self.log.info("******** Entering username ********")
        self.lp.set_password(self.password)
        self.log.info("******** Entering password ********")
        self.lp.click_login()
        self.log.info("******** Clicking Sign in button ********")
        self.aug = AppUserGuide(self.driver)
        self.log.info("******** Application is now on 'User guide' screen ********")
        self.aug.app_user_guide()
        self.log.info("******** Clicking skip ********")
        self.oc = DrIQHome(self.driver)
        self.log.info("******** Application is now on 'Dr.iQ Home' screen ********")
        self.oc.click_online_consultation()
        self.log.info("******** Clicking 'Online Consultation' module ********")
        self.oc = OnlineConsultation(self.driver)
        self.log.info("******** Application is now on 'Online Consultation' screen ********")
        self.oc.women_health_and_contraception_module()
        self.log.info("******** Clicking 'Women's Health and Contraception' module ********")
        self.con = Contraception(self.driver)
        self.log.info("******** 'Contraception' sub-modules ********")
        self.con.contraception()
        self.log.info("******** Clicking sub-module 'Contraception'********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = ConsultationForMyself(self.driver)
        self.log.info("******** Before we begin, please can you tell us who this e-consultation is for ********")
        self.con.consultation_for_myself()
        self.log.info("******** Selecting 'This e-consultation is for myself' option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = SelectTheProblem(self.driver)
        self.log.info("******** Before we begin, we just want to check your suitability for an online consultation' screen ********")
        self.con.select_option5()
        self.log.info("******** Selecting option no 05 ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = SelectPregnancy(self.driver)
        self.log.info("******** 'Please select one of the following statements' screen ********")
        self.con.select_not_pregnant()
        self.log.info("******** Selecting 1st option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = MedicalConditions(self.driver)
        self.log.info("******** 'Have you ever suffered from any of the following medical conditions?' screen ********")
        self.con.select_medical_conditions()
        self.log.info("******** Selecting medical conditions ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = SufferFromMigraines(self.driver)
        self.log.info("******** 'Do you suffer from migraines or severe headaches? screen ********")
        self.con.select_yes()
        self.log.info("******** Selecting 'Yes' option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = SufferingFromAura(self.driver)
        self.log.info("******** Do you suffer from Aura?' screen ********")
        self.con.select_yes()
        self.log.info("******** Selecting 'Yes' option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = SchedulingOfAnyMajorSurgery(self.driver)
        self.log.info("******** 'Are you scheduled for any major surgery in the next 12 months or have had any major surgery in the past 2 months?' screen ********")
        self.driver.implicitly_wait(10)
        self.con.select_yes()
        self.log.info("******** Selecting 'Yes' option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = EnterInfo(self.driver)
        self.log.info("******** 'Please provide more information about this' screen ********")
        self.con.enter_info(self.info)
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = ImmediateFamilyProblems(self.driver)
        self.log.info("******** 'Has anyone in your immediate family had any of the following:' screen********")
        self.con.select_yes()
        self.log.info("******** Selecting 'Yes' option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = FamilyDiagnosisInfo(self.driver)
        self.log.info("******** 'Please tell us who in your family was affected and at what age and what the diagnosis was?' screen ********")
        self.con.enter_relationship(self.relationship)
        self.log.info("******** Entering 'Relationship to you' ********")
        self.con.enter_age(self.age)
        self.log.info("******** Entering 'Age of family member' ********")
        self.con.enter_diagnosis(self.diagnosis)
        self.log.info("******** Entering 'Diagnosis' ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = FamilyMemberHasCancers(self.driver)
        self.log.info("******** 'Has anyone in your immediate family had any of the following cancers:' screen ********")
        self.con.select_yes()
        self.log.info("******** Selecting 'Yes' option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        # REPETITION OF SCREEN SO METHOD IS REUSABLE
        self.con = FamilyDiagnosisInfo(self.driver)
        self.log.info("******** 'Please tell us who in your family was affected and at what age and what the diagnosis was?' screen ********")
        self.con.enter_relationship(self.relationship)
        self.log.info("******** Entering 'Relationship to you' ********")
        self.con.enter_age(self.age)
        self.log.info("******** Entering 'Age of family member' ********")
        self.con.enter_diagnosis(self.diagnosis)
        self.log.info("******** Entering 'Diagnosis' ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = SelectMedications(self.driver)
        self.log.info("******** 'Please tick if you are taking any of the following medications' screen ********")
        self.con.select_medications()
        self.log.info("******** Selecting medications ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = AllergiesToMedications(self.driver)
        self.log.info("******** 'Do you have allergies to any medications?' screen ********")
        self.con.select_yes()
        self.log.info("******** Selecting 'Yes' option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        # REPETITION OF SCREEN SO METHOD IS REUSABLE.
        self.con = EnterInfo(self.driver)
        self.log.info("******** 'Please provide more information about this' screen ********")
        self.con.enter_info(self.info)
        self.log.info("******** Entering information ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = CurrentSmokingStatus(self.driver)
        self.log.info("******** 'We need to know about your current smoking status' screen ********")
        self.con.current_smoker()
        self.log.info("******** Selecting 'Current smoker' option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = CigaretteQuantity(self.driver)
        self.log.info("******** 'How many cigarettes do you smoke each day?' screen ********")
        self.con.select_option2()
        self.log.info("******** Selecting 2nd option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = SelectNoOption(self.driver)
        self.con.select_no()
        self.log.info("******** Selecting 'No' option ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = CalculateBMI(self.driver)
        self.log.info("******** 'Please enter your height & weight below to calculate BMI' screen ********")
        self.con.enter_height_feet_value(self.feet)
        self.log.info("******** Entering 'Feet' ********")
        self.con.enter_height_inch_value(self.inch)
        self.log.info("******** Entering 'Inch' ********")
        self.con.switch_weight()
        self.log.info("******** Clicking on 'Switch to kg' to switch weight ********")
        self.con.enter_weight_in_kg(self.weight_in_kg)
        self.log.info("******** Entering 'Weight' in Kg ********")
        self.con.calculate_bmi()
        self.log.info("******** Clicking 'Calculate' button ********")
        self.driver.implicitly_wait(10)
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = EnterCurrentPill(self.driver)
        self.log.info("******** 'Please tell us the name of the pill you are currently taking?' ********")
        self.con.enter_pill(self.pill)
        self.log.info("******** Entering pill ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = OtherInfo(self.driver)
        self.log.info("******** 'Please tell us if there is any other information that you would like us to have or write N/A' screen ********")
        self.con.enter_other_info(self.other_info)
        self.log.info("******** Entering additional information ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.om = SelectPharmacy(self.driver)
        self.log.info("******** Application is now on 'Please tell us which pharmacy you would like us to send your prescription to:' screen ********")
        self.om.select_pharmacy()
        self.log.info("******** Clicking 'Select Pharmacy Name' ********")
        self.om = PharmacySearchByPostCode(self.driver)
        self.log.info("******** Application is now on 'Pharmacy Search' screen. Searching pharmacy by postcode ********")
        self.om.click_search_by_postcode()
        self.log.info("******** Clicking 'Search by postcode' textbox ********")
        self.om.enter_postcode(self.postcode)
        self.log.info("******** Entering postcode ********")
        self.om.click_search()
        self.log.info("******** Clicking 'Search' button ********")
        self.om.select_postcode()
        self.log.info("******** Selecting post code from the list ********")
        self.om = EnterPreferredPharmacy(self.driver)
        self.log.info("******** 'Enter Preferred Pharmacy' ********")
        self.om.enter_preferred_pharmacy()
        self.log.info("******** Clicking 'Enter Preferred Pharmacy' ********")
        self.om.enter_pharmacy_details(self.pharmacy_details)
        self.log.info("******** Entering 'Pharmacy Details' ********")
        self.om.click_ok()
        self.log.info("******** Clicking 'Ok' button ********")
        self.con = NextButton(self.driver)
        self.con.click_next()
        self.log.info("******** Clicking 'Next' button ********")
        self.con = FinishPage(self.driver)
        self.log.info("******** Application is now on End screen to submit the online consultation request ********")
        self.con.click_finish()
        self.log.info("******** Clicking 'Finish' button to submit the online consultation ********")
        self.con = RequestConfirmationMenu(self.driver)
        self.log.info("******** After clicking 'Finish' button a 'Medication(s) ordered successfully' confirmation menu appears ********")
        self.con.click_ok()
        self.log.info("******** Clicking 'Ok' button ********")
        self.con = BackButton(self.driver)
        self.con.click_back()
        self.log.info("******** Clicking back button. Application is now on 'Online Consultation' screen. Contraception request submitted successfully. ********")
        self.driver.quit()

    @pytest.mark.sanity
    def test_contraception_web(self, setup_web):
        self.driver = setup_web
        self.driver.get(self.baseURL)
        self.lp = DrIQPWDLogin(self.driver)
        self.log.info("******** Dr.iQ Login page ********")
        self.lp.set_username(self.username_pwd)
        self.log.info("******** Entering username ********")
        self.lp.set_password(self.password_pwd)
        self.log.info("******** Entering password ********")
        self.lp.click_login()
        self.log.info("******** Clicking Sign in button. signing in to the PWD. ********")
        act_title = self.driver.title
        print(act_title)
        if act_title == "Dr_iQ | Dashboard":
            assert True
        else:
            assert False
        self.oc = DrIQPWDHome(self.driver)
        self.log.info("******** Dr.iQ Home ********")
        self.oc.click_online_consultations()
        self.log.info("******** Clicking on 'Online Consultations' tile ********")
        oc_title = self.driver.title
        print(oc_title)
        if oc_title == "Dr_iQ | Online Consultations":
            assert True
        else:
            assert False
        self.oc = OnlineConsultationsListingPage(self.driver)
        self.log.info("******** Dr.iQ Online Consultations Requests page ********")
        self.driver.implicitly_wait(10)
        self.oc.view_oc_request()
        self.log.info("******** Viewing online consultation request ********")
        self.oc = OnlineConsultationDetailPage(self.driver)
        self.log.info("******** Dr.iQ Online Consultations Details page ********")
        self.oc.enter_message(self.message)
        self.log.info("******** Entering message ********")
        self.oc.process_request()
        self.log.info("******** Processing online consultation request ********")
        self.oc = OutcomePopup(self.driver)
        self.log.info("******** 'What was the outcome of this OC?' menu ********")
        self.oc.select_oc_outcome()
        self.log.info("******** Selecting 'Closed in OC' option ********")
        self.driver.implicitly_wait(10)
        self.oc.click_submit()
        self.log.info("******** Clicking 'Submit' button ********")
        self.driver.close()
        self.log.info("******** Closing the driver after successful completion of test ********")




















