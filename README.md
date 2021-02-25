# HW6
## 0. Repeat everything I coded during the class.
## 0. Interview QQQQ! : Interview Q&A
## 0* Look through the list of EC methods 
## 0* Look through official doc for Slate Element Exception: 
https://www.seleniumhq.org/exceptions/stale_element_reference.jsp

## 1. Create a window handling test case from the class and verify that user can open amazon applications from Terms of Conditions
```features/tests/amazon_application.feature```

https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 

Scenario: User can open and close Amazon Applications
 Given Open Amazon T&C page 
 When Store original windows
 And Click on Amazon applications link (*see image below)
 And Switch to the newly opened window
 Then Amazon app page is opened
 And User can close new window and switch back to original


## 2*. [Loops] Make a test case which:
```features/tests/best_sellers.feature```

Clicks on Best Sellers link on the top menu
Clicks on each top link and verify that new page opens

Note: You can verify that the page opened by comparing the text: text of the link should be in the header text ⇒ ⇒ ⇒ 
