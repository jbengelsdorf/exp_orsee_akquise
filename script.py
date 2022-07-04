import alfred3 as al
from thesmuggler import smuggle

exp = al.Experiment()

content = smuggle("files/content.py")
informed_consent = smuggle("files/informed_consent.py")
registration = smuggle("files/exp_registration.py")


@exp.member
class WelcomePage(al.Page):
    title = "Herzlich Willkommen!"
    name = "welcome"

    def on_exp_access(self):
        self += al.Text(path="files/welcome.md")
        self += al.Alert(text=content.alert)


@exp.member
class ExperimentStart(al.ForwardOnlySection):
    def on_exp_access(self):
        self += informed_consent.InformedConsent(
            content=content.informed_consent_content,
            # info_sheet_path=self.exp.subpath("files/info_sheet.pdf"),
            name="informed_consent"
        )

        self += registration.RegistrationPage(
            content=content.registration_page_content,
            register_name=True,
            register_birth_date=False,
            register_email=True,
            register_phone=True,
            register_iban=False,
            register_address=False,
            register_various=False,
            register_payout=False,
        )


@exp.as_final_page
class EndPage(al.Page):
    name = "final_page"
    title = "Vielen Dank für Ihre Teilnahme!"

    def on_exp_access(self):
        self += al.Text(":mortar_board:", font_size=70, align="center")
        self += al.Text(content.contact, align="center")


if __name__ == "__main__":
    exp.run()
