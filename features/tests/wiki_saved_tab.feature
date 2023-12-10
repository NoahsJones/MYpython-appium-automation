# Created by noahsj at 12/6/2023
Feature: Saved tab
  # Enter feature description here

  Scenario: Log into wikipedia account
    Given log in page is opened
    When log in (User: njones66 Password: Letter2021)
    And turn off reading sync
    Then verify Njones66 is logged in