import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome()
    def test_2_adding_user_success(self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Adding User
        browser.find_element(By.CLASS_NAME,"firstLevelMenu").click() # klik button menu Admin
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click() # klik button Add
        time.sleep(2)
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Varmaa Rajeshh") # isi nama
        time.sleep(2)
        browser.find_element(By.ID,"systemUser_userName").send_keys("3admin123") # isi username
        time.sleep(2)
        browser.find_element(By.ID,"systemUser_password").send_keys("admin1239") # isi password
        time.sleep(2)
        browser.find_element(By.ID,"systemUser_confirmPassword").send_keys("admin1239") # isi password
        time.sleep(2)
        browser.find_element(By.NAME,"btnSave").click() # klik tsave
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID,"welcome").text

        self.assertIn('Welcome', response_data)

    def test_3_Search_found_by_Employee_name (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Adding User
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_employee_name_empName").send_keys("Varmaa Rajeshh") # isi nama
        time.sleep(2)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,".odd > td:nth-child(3) > a:nth-child(1)").text
        #response_message = browser.find_element(By.ID,"welcome").text

        self.assertIn('Varmaa', response_data)
        #self.assertEqual(response_message, 'Welcome Tushar')

    def test_4_Search_not_found_by_Employee_name (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Adding User
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_employee_name_empName").send_keys("sfsfsdfsdfsdf") # isi nama
        time.sleep(2)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#resultTable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)").text

        self.assertIn('No Records Found', response_data)

    def test_5_Search_found_by_Supervisor_Name  (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Adding User
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_supervisor_name").send_keys("Cassidy Hope") # isi nama
        time.sleep(2)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,".odd > td:nth-child(8)").text
        #response_message = browser.find_element(By.ID,"welcome").text

        self.assertIn('Cassidy Hope', response_data)
        #self.assertEqual(response_message, 'Welcome Tushar')

    def test_6_Search_found_by_Id (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Searching
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_id").send_keys("0054") # isi ID
        time.sleep(2)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"td.left:nth-child(2) > a:nth-child(1)").text

        self.assertIn('0054', response_data)

    def test_7_Search_found_by_Job_Title (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Searching
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_job_title").click()
        time.sleep(3)        
        browser.find_element(By.CSS_SELECTOR,"#empsearch_job_title > option:nth-child(8)").click()
        time.sleep(2)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"td.left:nth-child(5)").text

        self.assertIn('Database Administrator', response_data)

    def test_8_Search_found_by_Employment_Status (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Searching
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_employee_status").click()
        time.sleep(3)        
        browser.find_element(By.CSS_SELECTOR,"#empsearch_employee_status > option:nth-child(3)").click()
        time.sleep(2)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"tr.odd:nth-child(1) > td:nth-child(6)").text
        self.assertIn('Full-Time Contract', response_data)

    def test_9_Search__found_by_Sub_Unit (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Searching
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_sub_unit").click()
        time.sleep(3)        
        browser.find_element(By.CSS_SELECTOR,"#empsearch_sub_unit > option:nth-child(2)").click()
        time.sleep(2)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"tr.odd:nth-child(1) > td:nth-child(7)").text
        self.assertIn('Administration', response_data)

    def test_10_Add_Employee_success(self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Adding User
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click() # klik button Add
        time.sleep(2)

        browser.find_element(By.CSS_SELECTOR,"#firstName").send_keys("Dewa") # isi nama
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR,"#lastName").send_keys("Pujangga") # isi nama
        time.sleep(2)
        browser.find_element(By.ID,"btnSave").click() # klik tsave
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#pdMainContainer > div:nth-child(1) > h1:nth-child(1)").text
        self.assertIn('Personal Details', response_data)

    def test_11_Assign_Leave_with_insufficient_balance(self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Adding User
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click() # klik button menu Leave
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_assignLeave").click() # klik button apply
        time.sleep(2)
        browser.find_element(By.ID,"assignleave_txtEmployee_empName").send_keys("Jasmine Morgan")
        time.sleep(2)
        browser.find_element(By.ID,"assignleave_txtLeaveType").click()
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR,"#assignleave_txtLeaveType > option:nth-child(10)").click()
        time.sleep(2)
        browser.find_element(By.ID,"assignleave_txtFromDate").click()
        time.sleep(1)
        browser.find_element(By.ID,"assignleave_txtFromDate").send_keys("2022-05-01") # isi tanggal
        time.sleep(1)
        browser.find_element(By.ID,"assignleave_txtFromDate").send_keys(Keys.ENTER) 
        time.sleep(1)
        browser.find_element(By.ID,"assignleave_txtToDate").clear()
        time.sleep(1)
        browser.find_element(By.ID,"assignleave_txtToDate").send_keys("2022-05-05") # isi tanggal
        time.sleep(2)
        browser.find_element(By.ID,"assignleave_txtToDate").send_keys(Keys.ENTER)
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"#assignBtn").click() # klik tsave
        time.sleep(3)
       

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#leaveBalanceConfirm > div:nth-child(2)").text
        self.assertIn('sufficient leave balance', response_data)

    def test_12_Unfill_all_Assign_Leave_required_field_(self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Adding User
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click() # klik button menu Leave
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_assignLeave").click() # klik button apply
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR,"#assignBtn").click() # klik tsave
        time.sleep(3)
       

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#frmLeaveApply > fieldset:nth-child(1) > ol:nth-child(1) > li:nth-child(1) > span:nth-child(3)").text
        response_data2 = browser.find_element(By.CSS_SELECTOR,"#frmLeaveApply > fieldset:nth-child(1) > ol:nth-child(1) > li:nth-child(2) > span:nth-child(3)").text
        response_message = browser.find_element(By.CSS_SELECTOR,"#frmLeaveApply > fieldset:nth-child(1) > ol:nth-child(1) > li:nth-child(4) > span:nth-child(3)").text
        response_message2 = browser.find_element(By.CSS_SELECTOR,"#frmLeaveApply > fieldset:nth-child(1) > ol:nth-child(1) > li:nth-child(5) > span:nth-child(3)").text

        self.assertIn('Invalid', response_data)
        self.assertIn('Required', response_data2)
        self.assertEqual(response_message, 'Should be a valid date in yyyy-mm-dd format')
        self.assertEqual(response_message2, 'Should be a valid date in yyyy-mm-dd format')

    def test_13_Adding_Holiday_success(self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Adding User
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click() # klik button menu Leave
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_Configure").click() # klik button apply
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_viewHolidayList").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID,"holiday_description").send_keys("Lebaran")
        time.sleep(2)
        browser.find_element(By.ID,"holiday_date").click()
        time.sleep(1)
        browser.find_element(By.ID,"holiday_date").send_keys("2022-10-01") # isi tanggal
        time.sleep(1)
        browser.find_element(By.ID,"holiday_date").send_keys(Keys.ENTER)        
        browser.find_element(By.ID,"holiday_recurring").click()
        time.sleep(1)
        browser.find_element(By.ID,"holiday_length").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#holiday_length > option:nth-child(1)").click()
        time.sleep(1)
        browser.find_element(By.CLASS_NAME,"savebutton").click()
        time.sleep(1)
       

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"div.inner:nth-child(1)").text
        self.assertIn('Lebaran', response_data)


    def test_14_Adding_Holiday_success(self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Adding User
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click() # klik button menu Leave
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_Entitlements").click() # klik sub menu button
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_addLeaveEntitlement").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(1)
              

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"span.validation-error:nth-child(4)").text
        response_message = browser.find_element(By.CSS_SELECTOR,"span.validation-error:nth-child(3)").text

        self.assertIn('Required', response_data)
        self.assertEqual(response_message, 'Required')


    def test_15_Add_Leave_Entitlement_success(self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Adding User
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click() # klik button menu Leave
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_Entitlements").click() # klik sub menu button
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_addLeaveEntitlement").click()
        time.sleep(1)
        browser.find_element(By.ID,"entitlements_employee_empName").send_keys("David Morris")
        time.sleep(1)
        browser.find_element(By.ID,"entitlements_employee_empName").send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element(By.ID,"entitlements_leave_type").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#entitlements_leave_type > option:nth-child(4)").click()
        time.sleep(1)
        browser.find_element(By.ID,"entitlements_entitlement").send_keys("2")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(10)
        browser.find_element(By.ID,"dialogUpdateEntitlementConfirmBtn").click()
        time.sleep(5)
              

        response_data = browser.find_element(By.CSS_SELECTOR,"td.left:nth-child(2)").text
        self.assertIn('Added', response_data)

    def test_16_Keep_Employee_name_field_Blank_hit_view (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Searching
        browser.find_element(By.ID,"menu_time_viewTimeModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"menu_time_Timesheets").click()
        time.sleep(3)        
        browser.find_element(By.ID,"menu_time_viewEmployeeTimesheet").click()
        time.sleep(3)   
        browser.find_element(By.ID,"btnView").click()
        time.sleep(3)
        

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"span.validation-error").text
        self.assertIn('Required', response_data)

    def test_17_View_Employee_timesheet_not_found (self):
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Steps to Searching
        browser.find_element(By.ID,"menu_time_viewTimeModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"employee").click()
        browser.find_element(By.ID,"employee").send_keys("David Morris")
        time.sleep(3)

        browser.find_element(By.ID,"btnView").click()
        time.sleep(3)
        

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,".message").text
        self.assertIn('No Timesheets Found', response_data)


    def test_18_Punch_in_and_punc_out_success (self):
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

        # Punch in
        browser.find_element(By.ID,"menu_time_viewTimeModule").click() # klik button menu PIM
        time.sleep(1)
        browser.find_element(By.ID,"menu_attendance_Attendance").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_attendance_punchIn").click()
        time.sleep(2)
        browser.find_element(By.ID,"attendance_date").clear()
        time.sleep(1)
        browser.find_element(By.ID,"attendance_date").send_keys("2022-08-08")
        time.sleep(1)
        browser.find_element(By.ID,"attendance_date").send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element(By.ID,"attendance_time").clear()
        browser.find_element(By.ID,"attendance_time").send_keys("15:00")
        time.sleep(1)
        browser.find_element(By.ID,"attendance_note").send_keys("Meeting begin")
        time.sleep(1)
        browser.find_element(By.ID,"btnPunch").click()
        time.sleep(5)

        # Punch Out
        browser.find_element(By.ID,"attendance_date").clear()
        time.sleep(1)
        browser.find_element(By.ID,"attendance_date").send_keys("2022-08-09")
        time.sleep(1)
        browser.find_element(By.ID,"attendance_date").send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element(By.ID,"attendance_time").clear()
        browser.find_element(By.ID,"attendance_time").send_keys("15:00")
        time.sleep(1)
        browser.find_element(By.ID,"attendance_note").clear()
        time.sleep(1)
        browser.find_element(By.ID,"attendance_note").send_keys("Meeting ended")
        time.sleep(1)
        browser.find_element(By.ID,"btnPunch").click()
        time.sleep(5)
        

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,".head > h1:nth-child(1)").text
        self.assertIn('Punch In', response_data)

    def test_19_Success_Adding_Candidate (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click() # klik button menu Recruit
        time.sleep(3)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(3)        

        browser.find_element(By.ID,"addCandidate_firstName").send_keys("Dewa")
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_lastName").send_keys("Pujangga")
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_email").send_keys("Pujangga@gg.com")
        time.sleep(2)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#menu_recruitment_viewCandidates").text

        self.assertIn('Candidate', response_data)

    def test_20_Put_incorrect_email_Format (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click() # klik button menu Recruit
        time.sleep(3)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(3)        

        browser.find_element(By.ID,"addCandidate_firstName").send_keys("Dewa")
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_lastName").send_keys("Pujangga")
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_email").send_keys("Pujanggagg.com")
        time.sleep(2)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"span.validation-error").text
        self.assertIn('Expected format: admin@example.com', response_data)

    def test_21_Success_Editing_Contact_details (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu_pim_viewMyDetails").click() # klik button menu Recruit
        time.sleep(3)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(2)        
        browser.find_element(By.ID,"personal_cmbMarital").send_keys("Dewa")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#personal_cmbMarital > option:nth-child(3)").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(4)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#pdMainContainer > div:nth-child(1) > h1:nth-child(1)").text
        self.assertIn('Personal Details', response_data)


    def test_22_Put_incorrect_email_Format (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu_pim_viewMyDetails").click() # klik button menu Recruit
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"#sidenav > li:nth-child(2) > a:nth-child(1)").click()
        time.sleep(2)     
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(2)   
        browser.find_element(By.ID,"contact_emp_work_email").click()
        time.sleep(2)
        browser.find_element(By.ID,"contact_emp_work_email").clear()
        time.sleep(2)
        browser.find_element(By.ID,"contact_emp_work_email").send_keys("asdsd.dasd.co")
        time.sleep(2)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(4)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"span.validation-error").text
        self.assertIn('Expected format: admin@example.com', response_data)

    def test_23_Search_found_by_Job_title (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu__Performance").click() # klik button menu Recruit
        time.sleep(3)
        browser.find_element(By.ID,"menu_performance_Configure").click()
        time.sleep(1)     
        browser.find_element(By.ID,"menu_performance_searchKpi").click()
        time.sleep(2)   
        browser.find_element(By.ID,"kpi360SearchForm_jobTitleCode").click()
        time.sleep(2)  
        browser.find_element(By.CSS_SELECTOR,"#kpi360SearchForm_jobTitleCode > option:nth-child(20) ").click()
        time.sleep(2)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#frmList_ohrmListComponent").text
        self.assertIn('QA Engineer', response_data)


    def test_24_Search_found_by_Job_title (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu__Performance").click() # klik button menu Recruit
        time.sleep(3)
        browser.find_element(By.ID,"menu_performance_Configure").click()
        time.sleep(1)     
        browser.find_element(By.ID,"menu_performance_addPerformanceTracker").click() #Klik sub menu trackers
        time.sleep(2)   
        browser.find_element(By.ID,"btnAdd").click() #klik add button
        time.sleep(2)  
        browser.find_element(By.ID,"addPerformanceTracker_tracker_name").send_keys("Final interview") #input tracker name
        time.sleep(2)
        browser.find_element(By.ID,"addPerformanceTracker_employeeName_empName").send_keys("David Morris") #input tracker name
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR,"#addPerformanceTracker_availableEmp > option:nth-child(4)").click()
        time.sleep(2)
        browser.find_element(By.ID,"btnAssignEmployee").click()
        time.sleep(2)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#frmList_ohrmListComponent").text
        self.assertIn('David Morris', response_data)


    def test_25_Access_to_quick_launch_Assign_Leave (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu_dashboard_index").click() # klik button menu dashboard
        time.sleep(3)         
        browser.find_element(By.CSS_SELECTOR,".quickLaungeContainer > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)").click() #klik add button
        time.sleep(2)  
        

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,".head > h1:nth-child(1)").text
        self.assertIn('Assign Leave', response_data)


    def test_26_Access_to_quick_launch_Apply_Leave (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu_dashboard_index").click() # klik button menu dashboard
        time.sleep(3)         
        browser.find_element(By.CSS_SELECTOR,".quickLaungeContainer > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)").click() #klik add button
        time.sleep(2)  
        

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,".head > h1:nth-child(1)").text
        self.assertIn('Apply Leave', response_data)

    def test_27_Search_found_by_name (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu_directory_viewDirectory").click() # 
        time.sleep(3)         
        browser.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys("David Morris") # 
        time.sleep(3)         
        browser.find_element(By.ID,"searchBtn").click() #klik search
        

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#resultBox").text
        self.assertIn('David Morris', response_data)

    def test_28_Search_found_Job_Title (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu_directory_viewDirectory").click() # 
        time.sleep(3)         
        browser.find_element(By.ID,"searchDirectory_job_title").click()  #Klik job title
        time.sleep(2)         
        browser.find_element(By.CSS_SELECTOR,"#searchDirectory_job_title > option:nth-child(4)").click() 
        time.sleep(2)         
        browser.find_element(By.ID,"searchBtn").click() #klik search
        

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#resultBox").text
        
        self.assertIn('Chief Executive Officer', response_data)

    def test_29_Search_found_in_access_records (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu_maintenance_purgeEmployee").click() # 
        time.sleep(3)         
        browser.find_element(By.ID,"menu_maintenance_accessEmployeeData").click()  #Klik Access records
        time.sleep(2)         
        browser.find_element(By.ID,"confirm_password").send_keys("admin123") # input password
        time.sleep(2)         
        browser.find_element(By.CSS_SELECTOR,"div.input-field:nth-child(2) > input:nth-child(2)").click() 
        time.sleep(2)  

        browser.find_element(By.ID,"employee_empName").send_keys("David")
        time.sleep(2)
        browser.find_element(By.ID,"employee_empName").send_keys(Keys.TAB)
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR,".search_employee").click() #klik search
        time.sleep(5)
        

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#full_name").text
        self.assertIn('David Morris', response_data)

    def test_30_Update_status_success (self): 
        # steps to Login as Admin
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.NAME,"Submit").click() # klik tombol sign in
        time.sleep(1)

       
        browser.find_element(By.ID,"menu_buzz_viewBuzz").click() # klik buzz menu
        time.sleep(2)         
        browser.find_element(By.ID,"createPost_content").send_keys("Hello world")
        time.sleep(2)         
        browser.find_element(By.ID,"postSubmitBtn").click()
        time.sleep(2) 
     

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#buzz").text
        self.assertIn('Hello world', response_data)



    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
