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


    rule detect_keywords
    {
        strings:
            	${keyword0} = "drug" ascii nocase
        condition:
            any of them
    }
    

    rule detect_keywords
    {
        strings:
            	${keyword0} = "drug" ascii nocase
        condition:
            any of them
    }
    

    rule detect_keywords
    {
        strings:
            	${keyword0} = "drug" ascii nocase
        condition:
            any of them
    }
    

    rule detect_keywords
    {
        strings:
            	${keyword0} = "drug" ascii nocase
        condition:
            any of them
    }
    

    rule detect_keywords
    {
        strings:
            	${keyword0} = "drug" ascii nocase
        condition:
            any of them
    }
    

    rule detect_keywords
    {
        strings:
            	${keyword0} = "drug" ascii nocase
        condition:
            any of them
    }
    

    rule detect_keywords
    {
        strings:
            	${keyword0} = "drug" ascii nocase
        condition:
            any of them
    }
    

    rule detect_keywords
    {
        strings:
            	${keyword0} = "drug" ascii nocase
        condition:
            any of them
    }
    

    rule detect_keywords
    {
        strings:
            	${keyword0} = "drug" ascii nocase
        condition:
            any of them
    }
    

    rule detect_keywords
    {
        strings:
            	${keyword0} = "drug" ascii nocase
        condition:
            any of them
    }
    
