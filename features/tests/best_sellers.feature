# Created by Joonil at 2/25/21
Feature: Test Scenarios for Clicking on every top link in the Amazon best sellers page

  Scenario: The Amazon best sellers page have top links, each page opens when user clicks on them
    Given Open Amazon page
    When Click on the best sellers link
    Then Click on every top link, and verify pages get properly open

