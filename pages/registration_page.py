from selene import browser, have, command
import resourses


class RegistrationPage:

    def __init__(self):
        self.registered_user_data = (
            browser.element(".modal-content").element("table").all("tr").all("td").even
        )
        self.month_of_birth = browser.element(".react-datepicker__month-select")

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_second_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def select_gender(self, gender):
        browser.element(f"[name=gender][value={gender}]+label").click()
        return self

    def fill_phone_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    def fill_date_of_birth(self, month, year, day):
        browser.element("#dateOfBirthInput").click()
        self.month_of_birth.click()
        self.month_of_birth.all("option").element_by(have.exact_text(month)).click()
        browser.element(".react-datepicker__year-select").send_keys(year)
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    def fill_subjects(self, value):
        browser.element("#subjectsInput").type(value).press_enter()
        return self

    def fill_hobbies(self, hobby):
        browser.all("[for^=hobbies-checkbox]").element_by(have.text(hobby)).click()
        return self

    def upload_picture(self, photo):
        browser.element("#uploadPicture").send_keys(resourses.path(photo))
        return self

    def fill_current_address(self, address):
        browser.element("#currentAddress").type(address).perform(command.js.scroll_into_view)
        return self

    def fill_state(self, name):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_city(self, city):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(city)
        ).click()
        return self

    def submit_form(self):
        browser.element("#submit").press_enter()
        return self

    def should_registered_user_info_with(
        self,
        full_name,
        email,
        gender,
        phone,
        date_of_birth,
        area_of_study,
        hobby,
        photo,
        address,
        city_and_state,
    ):
        browser.element(".modal-content").element("table").all("tr").all(
            "td"
        ).even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                area_of_study,
                hobby,
                photo,
                address,
                city_and_state,
            )
        )