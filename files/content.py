alert = """
Wir hoffen, dass wir Sie von einer Registrierung bei Orsee3 überzeugen konnten.<br> 
Um die Registrierung vorzunehmen, klicken Sie bitte auf "Weiter".
"""

info_database = """
Die in der Versuchspersonendatenbank der Abteilung für Wirtschafts- und Sozialpsychologie des 
Georg-Elias-Müller-Institutes für Psychologie erfassten Daten dienen ausschließlich der 
Organisation von wissenschaftlichen Experimenten. Diese Daten werden nicht an Dritte 
weitergegeben. Wir benutzen die Daten zu den folgenden Zwecken: 

+ um die Versuchspersonen über neue Labor- oder Onlineexperimente zu informieren und dazu 
einzuladen
+ um eine wissenschaftlich motivierte Auswahl von Versuchspersonen für bestimmte Experimente 
durchzuführen
+ um das Erscheinen bzw. Nicht-Erscheinen der angemeldeten Versuchspersonen bei Experimenten zu 
überprüfen

Es gibt keine Verknüpfung zwischen den im Experiment generierten Daten und den Daten in der 
Versuchspersonendatenbank.Versuchspersonen können jederzeit bestimmen, keine weiteren Einladungen 
zu Experimenten zu erhalten.
Auf Verlangen werden sämtliche erfassten Daten gelöscht. 
Hierfür ist eine formlose schriftliche Löschungsaufforderung per Email an folgende Adresse 
zu senden: gemi.orsee@googlemail.com"""

informed_consent_content = dict(
    title="Informationen für Teilnehmende",
    experimenter_in_charge="Dr. Christian Treffenstädt",
    experimenter_in_charge_email="treffenstaedt@psych.uni-goettingen.de",
    study_email="abt5exp@psych.uni-goettingen.de",
    consent_accept_label="Einwilligen",
    consent_reject_label="Ablehnen",

    # language=HTML
    introduction="""Liebe:r Wissenschaftsinteressierte,<br> 
    wir bitten Sie um Ihre Einwilligung in die 
    Erhebung und Verarbeitung der für die Orsee3-Registrierung notwendigen Daten.""",

    # language=HTML
    study_info="""<span style="font-size: 1.4em; "><b>Informationen zur Vergütung</b>
    </span>
    <br>
    Um Sie als Versuchsperson in unserer Datenbank registrieren zu können, benötigen wir 
    einige personenbezogene Informationen von Ihnen.
    Bei Fragen zur Studie wenden Sie sich bitte an 
    <span style="color: blue; ">{study_email}</span>. Verantwortlich für diese Datenerhebung ist 
    {experimenter_in_charge} ({experimenter_in_charge_email}).
    """,
    # language=HTML
    data_processing_info=""" <span style="font-size: 1.4em; "><b>Informationen zur 
    Datenverarbeitung</b></span> 
    <br>
    Explizit werden Sie auf der nächsten Seite gebeten, Ihren Vor- und 
    Nachnamen, Ihre E-Mail-Adresse und Ihre Telefonnummer anzugeben. 
    <br> <br>
    Die erfassten Daten dienen ausschließlich der Organisation von wissenschaftlichen 
    Experimenten. Diese Daten werden nicht an Dritte weitergegeben. Wir benutzen die Daten zu den 
    folgenden Zwecken: <ul>
    <li> um die Versuchspersonen über neue Labor- oder Onlineexperimente zu informieren und dazu 
    einzuladen.</li>
    <li> um eine wissenschaftlich motivierte Auswahl von Versuchspersonen für bestimmte Experimente 
    durchzuführen.</li>
    <li>um das Erscheinen bzw. Nicht-Erscheinen der angemeldeten Versuchspersonen bei Experimenten zu 
    überprüfen.</li>
    </ul>
    Es gibt keine Verknüpfung zwischen den im Experiment generierten Daten und den Daten in der 
    Versuchspersonendatenbank. Versuchspersonen können jederzeit bestimmen, keine weiteren 
    Einladungen zu Experimenten zu erhalten. Auf Verlangen werden sämtliche erfassten Daten 
    gelöscht. Hierfür ist eine formlose schriftliche Löschungsaufforderung per Email an folgende 
    Adresse zu senden: <span style="color: blue; ">gemi.orsee@googlemail.com</span>
    """,

    # info_sheet_link_text="Hinweisblatt nach Art. 13 DSGVO",
    # language=HTML
    consent=
    """<span style="font-size: 1.4em; "><b>Einwilligungserklärung</b></span>
    <br>
    Ich habe keine weiteren Fragen und willige hiermit in die 
    beschriebene Datenerhebung und -verarbeitung ein.
    """,

    consent_reject_title="Ablehnung der Teilnahme",
    consent_reject_icon="times-circle",

    # language=HTML
    consent_reject_message=
    """Sie haben nicht in die Teilnahme eingewilligt und damit die Registrierung abgebrochen.
    Sie können diese Seite nun schließen.
    <br><br>
    <b>Es werden keinerlei personenbezogene Informationen über Sie gespeichert.</b>
    <br><br>
    Falls Sie Fragen haben, melde Sie sich gerne unter <span style="color: blue; ">
    {study_email}</span>
    """
)

registration_page_content = dict(
    title="Registrierung",
    statustext="Um Ihre Registrierung zu abzuschließen, klicken Sie auf 'Weiter'.",
    instr_no_registration="Wir benötigen keine persönlichen Daten von Ihnen. "
                          "Sie können auf 'Weiter' klicken.",
    instr_registration="Bitte geben Sie die folgenden persönlichen Informationen ein.",
    first_name_instr="Vorname",
    last_name_instr="Nachname",
    birth_date_instr="Geburtsdatum",
    birth_date_pattern=r"^(0[1-9]|[12][0-9]|3[01])[-/.](0[1-9]|1[012])[-/.](19|20)\d\d$",
    birth_date_suffix="TT.MM.JJJJ",
    birth_date_match_hint="Dies ist der Match-Hinweis für das Feld Geburtsdatum.",
    email_instr="E-Mail-Adresse",
    email_pattern=r"[^@]+@[^@]+\.[^@]+",
    email_match_hint="Bitte geben Sie eine gültige E-Mail-Adresse ein.",
    iban_instr="IBAN",
    iban_pattern=r"^[A-Z]{2}[0-9]{2}(?:[ ]?[0-9]{4}){4}(?:[ ]?[0-9]{1,2})?$",
    iban_match_hint="Fehler: Bitte überprüfen Sie Ihre Eingabe.",
    bic_instr="BIC",
    bic_pattern=r"^[a-zA-Z]{6}[0-9a-zA-Z]{2}([0-9a-zA-Z]{3})?$",
    bic_match_hint="Fehler: Bitte überprüfen Sie Ihre Eingabe.",
    tax_office_instr="Sitz Ihres Finanzamtes",
    phone_instr="Telefonnummer",
    phone_pattern=r"^\+?(?:[0-9]\x20?){6,14}[0-9]$",
    phone_match_hint="Fehler: Bitte überprüfen Sie Ihre Eingabe.",
    street_instr="Straßenname",
    house_number_instr="Hausnummer",
    postal_code_instr="Postleitzahl",
    postal_code_pattern=r"(?i)^[a-z0-9][a-z0-9\- ]{0,10}[a-z0-9]$",
    postal_code_match_hint="Fehler: Bitte überprüfen Sie Ihre Eingabe.",
    city_instr="Ort",
    country_instr="Land",
    various_instr="Matrikelnummer",
    various_pattern=r"^..*$",  # Anything but empty
    various_match_hint="Fehler: Bitte überprüfen Sie Ihre Eingabe.",
    privacy_info="This is a dummy text for privacy information",
    repeated_title="Anscheinend haben Sie bereits an dem Experiment teilgenommen",
    repeated_text="This is a dummy text for the repeated participation page",
    repeated_participation_title="Erneute Teilnahme detektiert",
    repeated_participation_icon="times-circle",
    repeated_participation_message="Es tut uns leid, aber eine wiederholte Teilnahme an"
                                   " diesem Experiment ist nicht erlaubt. Ihre "
                                   "persönlichen Daten werden nicht gespeichert",
)

contact = """
Bei Anmerkungen oder Fragen können Sie uns gerne unter folgender E-Mail-Adresse kontaktieren: 
abt5exp@psych.uni-goettingen.de.<br>
"""