/*
    Yara.
*/

rule email_filter
{
        strings:
              $email_add = /\b[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)*\.[a-zA-Z-]+[\w-]\b/
        condition:
            any of them

}

rule detect_drugs
{
    strings:
        $drugs = "trouble"
    condition:
        $drugs
}
