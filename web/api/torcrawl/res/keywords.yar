
rule detect_keywords
{
    strings:
        	$c = "cerebral" ascii nocase
    condition:
        any of them
}

