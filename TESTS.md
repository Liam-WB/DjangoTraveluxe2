# Traveluxe | Tests

Return to [README.md](README.md)

---

Comprehensive testing has been done to ensure that the website's functions and features work flawlessly, and without issue.

## Directory of Contents

### Responsiveness Tests

### Browser Compatibility Tests

### Device Tests

### Code Validation
## * HTML Validation
## * CSS Validation
## * JavaScript Validation
## * Python

### Lighthouse Report

### Bugs
## * Resolved Bugs
## * Unresolved Bugs

### Features Tests

---

## Responsiveness Tests

This deployed Traveluxe website has underwent rigorous and frequent testing on multiple devices and screen sizes to ensure its responsiveness and adaptability. Developer Tools were utilized to simulate various screen sizes, enabling thorough examination of how the website behaves across different devices. Bootstrap classes and media queries have been implemented to achieve the desired design, ensuring that the website maintains its visual and functional integrity on all platforms, to create a positive user experience.

![Responsive](md_images/responsive.png)

### Different Screen Sizes

![PC](md_images/homepage.png)
![Laptop](md_images/laptop.png)
![Tablet](md_images/tablet.png)
![Phone](md_images/phone.png)

## Browser Compatibility Tests

The website was also tested on google chrome, microsoft edge, firefox and iOS safari. The website worked as intended.

## Code Validation

### HTML Validation

The website was tested on [W3C HTML Validator](https://validator.w3.org/nu), and the below listed HTML was checked for errors:

* base.html
* index.html
* post_detail.html
* post_form.html
* account_login,logout,signup.html

The results showed no major errors.

![HTML](md_images/HTML.png)

### CSS Validation

The website was tested on [W3C CSS Validator](https://jigsaw.w3.org/css-validator/), and the style.css file showed no errors.

![CSS](md_images/CSS.png)

### JavaScript Validation

No issues or errors were made present during JavaScript testing and validation.

### Python Validation

The following Python files were validated and checked with [Python Linter](https://pep8ci.herokuapp.com/):

#### market

* admin.py
* app.py
* forms.py
* models.py
* teste.py
* urls.py
* views.py

#### traveluxe

* settings.py
* urls.py

![plint1](md_images/plint1.png)
![plint2](md_images/plint2.png)
![plint3](md_images/plint3.png)
![plint4](md_images/plint4.png)
![plint5](md_images/plint5.png)
![plint6](md_images/plint6.png)
![plint7](md_images/plint7.png)
![plint8](md_images/plint8.png)
![plint9](md_images/plint9.png)

## Lighthouse Reports

The following pages were checked for lighthouse reports:

* index.html
* post_detail.html
* post_form.html
* account_login,logout,signup.html

![LH1](md_images/LH1.png)
![LH2](md_images/LH2.png)
![LH3](md_images/LH3.png)
![LH4](md_images/LH4.png)
![LH5](md_images/LH5.png)
![LH6](md_images/LH6.png)

## Bugs

### Resolved Bugs

#### Issue discovered where style changes were not applying to allauth form templates.

I wanted some of the form input sections to be hidden/removed. The issue was resolved temporarily by adding inline styles rather than through the template as the template would not change.

#### Issue discovered where a post could not be submitted due to a clash with user ID being used on the model.

This was resolved by creating the Author class earlier on, which also includes the form_valid() now.

### Unresolved Bugs

#### Issue discovered where not all alert messages show up green.

Some alerts show up green, whereas some do not. As the alerts still functioned properly, and alerts were not a priority at the time, I have not had the time to resolve this issue yet, or implement extra alerts, however with extra time I could have resolved this.

## Features Tests

All buttons, features, functions, forms, input boxes etc. were tested rigorously and properly throughout the development of Traveluxe.

Here is a list of the features tested throughout the development of this project:

### base.html (regardless of page, these should all function correctly)

* Navbar (style, dimensions, visibility)
* Navbar items (links, style, highlighting, changes based on authorisation)
* Logo (style, link)
* Navbar compact phone screen pop-out button (visibility, action)
* Footer (style, dimensions, visibility)
* Footer contents (readability, visibility)
* Socials Icons (links, style, highlighting)
* Alerts/messages (functioning properly, visibility)

### index.html

* Post List (style, dimensions, visibility, readability, links, link highlighting, information/detail, positioning, pagination)
* Post Links (highlighting, visibility, readability)
* Post Images (load times, visibility, visual aesthetic, positioning, suitability)
* Like counter (functioning correctly, visibility, readability)
* Date Time Field (functioning correctly, visibility, readability)

### post_detail.html

* Post Images (load times, visibility, visual aesthetic, positioning, suitability)
* Like section (functioning correctly, visibility, readability, changes based on authorisation)
* Comment section (functioning correctly, visibility, readability, changes based on authorisation)
* Post content (visibility, readability)

### post_form.html

* Form Input Boxes (taking the right values, displaying the right values, validating correct characters used, readability, visibility, functioning as intended, required if they are required)
* Submit Button (Redirecting to correct links, carrying out the correct processes, posting correct and accurate data, readability, visibility, highlighting)

### account_login,logout,signup.html

* Form Input Boxes (taking the right values, displaying the right values, validating correct characters used, readability, visibility, functioning as intended, required if they are required)
* Submit Button (Redirecting to correct links, carrying out the correct processes, posting correct and accurate data, readability, visibility, highlighting)

### Admin Panel

* CRUD Functionality

All items listed above passed their main objective of functioning as intended and contributing towards a positive user experience.

Return to [README.md](README.md)