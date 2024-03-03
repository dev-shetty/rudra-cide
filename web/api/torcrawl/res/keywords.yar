
    rule detect_keywords
    {
        strings:
            	$d = "drug" ascii nocase
        condition:
            any of them
    }
    
