"""Informed consent page

author: Christian Treffenstädt
updated: 2021-04-27

"""

import alfred3 as al

##########################
# - Section 2: Content - #
##########################

informed_consent_content = dict(
    title="Informed Consent",
    experimenter_in_charge="",
    experimenter_in_charge_email="",
    study_email="",
    consent_accept_label="Accept",
    consent_reject_label="Reject",

    # language=HTML
    introduction="""These are introductory sentences to the informed consent
    """,

    # language=HTML
    study_info=
    """<span style="font-size: large; "><b>Study Information</b>
    </span>
    This text should provide specific information about the study.
    <br><br>
    The experimenter in charge is: {experimenter_in_charge} 
    ({experimenter_in_charge_email}).
    <br><br>
    If you have any questions, please contact {study_email}
    """,

    # language=HTML
    data_processing_info=
    """This text should provide general information about our handling of the collected
    experimental data.
    
    """,

    # info_sheet_link_text="GDPR Information Sheet",

    # language=HTML
    consent=
    """<span style="font-size: large; "><b>Consent Regarding Data Collection and 
    Processing</b></span>
    <br>
    This text should provide the actual consent text
    <br><br>
    <b>Note:</b> If you click on 'Accept', the experiment will start immediately. Click 
    'Reject' to finish the experiment without any personal data being recorded.
    """,

    consent_reject_title="Consent: Rejected",
    consent_reject_icon="times-circle",

    # language=HTML
    consent_reject_message=
    """You have aborted the experiment.
    <br><br>
    You can close this page now.
    <br><br>
    If you have any questions, please mail us at <span style="color: blue; ">{study_email}</span>
    """
)


#################################
# - Section 3: Custom classes - #
#################################


class InformedConsent(al.Page):
    """Custom question to document participants' consent"""

    content = None

    def __init__(
            self,
            content=None,
            info_sheet_path=None,
            **kwargs
    ):
        super(InformedConsent, self).__init__(**kwargs)

        if content is not None:
            self.content = content

        if self.content is None:
            self.content = informed_consent_content

        if "title" not in kwargs:
            self.title = (f"<div align='center' style='font-size: 1.2em; "
                          f"margin-bottom: 25px;'>{self.content['title']}<div>")

        # if info_sheet_path is not None:
        #     self.info_sheet_path = info_sheet_path

        # if self.info_sheet_path is None:
        #     raise ValueError(
        #         f"Argument 'info_sheet_path' in {type(self).__name__} element "
        #         f"'{self.name}' is missing."
        #     )

        if self.content["study_email"] == "":
            raise ValueError(
                f"Variable 'study_mail' in content of {type(self).__name__} "
                f"element must not be empty."
            )

    def on_exp_access(self):

        # info_sheet_url = self.exp.ui.add_static_file(
        #     self.info_sheet_path,
        #     content_type="application/pdf"
        # )

        # Disable all forward type buttons
        self += al.Style("#forward_button {display: none;}")
        self += al.Style("#finish_button {display: none;}")

        if not self.content["introduction"] == "":
            self += al.Html(self.content["introduction"], width='wide')
            self += al.VerticalSpace("1em")

        info_text = self.content["study_info"].format(
            experimenter_in_charge=self.content["experimenter_in_charge"],
            experimenter_in_charge_email=self.content[
                "experimenter_in_charge_email"],
            study_email=self.content["study_email"]
        )

        self += al.Html(info_text, width='wide')
        self += al.VerticalSpace("1em")

        if not self.content["data_processing_info"] == "":
            self += al.Html(self.content["data_processing_info"], width='wide')
            self += al.VerticalSpace("1em")

        # self += al.Html(
        #     f'<a href="{info_sheet_url}" target="_blank">'
        #     f'{self.content["info_sheet_link_text"]}</a>',
        #     width='wide'
        # )

        self += al.Hline()

        self += al.Html(self.content["consent"], width='wide')
        self += al.VerticalSpace("1em")

        self += al.SubmittingButtons(
            f"<i class='fas fa-thumbs-up ml-0 mr-0' style='font-size: 1em;'></i> "
            f"{self.content['consent_accept_label']}",
            f"<i class='fas fa-thumbs-down ml-0 mr-0' style='font-size: 1em;'></i> "
            f"{self.content['consent_reject_label']}",
            name="consent",
            align="center",
            width="medium",
            font_size="big",
            button_style=["btn-outline-success", "btn-outline-danger"],
            description='Informed Consent: Accept or Reject'
        )

    def on_each_hide(self):
        if self.consent.input is None:
            return

        elif self.consent.input == 1:
            self.exp.session_status = 'Informed Consent: Accepted'

        elif self.consent.input == 2:
            self._experiment.session_status = 'Informed Consent: Rejected'

            self.exp.abort(
                reason=(
                    "Informed Consent: The participant has rejected the informed "
                    "consent statement. Aborting the Session."
                ),
                title=self.content["consent_reject_title"],
                icon=self.content["consent_reject_icon"],
                msg=self.content["consent_reject_message"].format(
                    study_email=self.content["study_email"])
            )
