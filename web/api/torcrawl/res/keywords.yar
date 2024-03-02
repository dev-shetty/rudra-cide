/*
    Yara.
*/

/*
    rule email_filter
    {
        meta:
            author = "@the-siegfried"
            score = 20
        strings:
              $email_add = /\b[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)*\.[a-zA-Z-]+[\w-]\b/
        condition:
            any of them

    }
*/

rule keyword_search
{
    meta:
        author = "@the-siegfried"
        score = 90

    strings:
        $a = "DNM" fullword wide ascii nocase

    condition:
        any of them
}