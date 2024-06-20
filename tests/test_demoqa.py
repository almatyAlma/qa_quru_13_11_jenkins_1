from pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    (
        registration_page.fill_first_name("firstName")
        .fill_second_name("lastName")
        .fill_email("test@gmail.com")
        .select_gender("Female")
        .fill_phone_number("7777777777")
        .fill_date_of_birth("July", "1991", "29")
        .fill_subjects("Computer Science")
        .fill_hobbies("Sports")
        .upload_picture("orig.jpg")
        .fill_current_address("Current Address")
        .fill_state("Haryana")
        .fill_city("Karnal")
        .submit_form()
    )

    registration_page.should_registered_user_info_with(
        "firstName lastName",
        "test@gmail.com",
        "Female",
        "7777777777",
        "29 July,1991",
        "Computer Science",
        "Sports",
        "orig.jpg",
        "Current Address",
        "Haryana Karnal",
    )