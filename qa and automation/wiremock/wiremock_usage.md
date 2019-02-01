#REQUEST MATCHING:

###URL matching:

```json
{
  "request": {
    "url": "/your/url?and=query", //or
    "urlPattern": "/your/([a-z]*)\\?and=query" //regex
  }
}
```

###Header matching:

```json
{
	"request": {
		"headers" : {
			"Content-Type": {
				"equalTo": "application/json", //or
				"contains": "json", //or
				"caseInsensitive": true
			},
			"other-header": {
				"matches": "^app.*json$", //regex
				"doesNotMatch": "^patata.*amigo$" //regex
			},
			"data-blob": {
				"binaryEqualTo": "1235DASDGSD" //equality for base 64
			},
		}
	}
}
```

###Basic auth:

```json
{
    "request": {
        "method": "GET",
        "url": "/basic-auth",
        "basicAuth" : {
            "username" : "user",
            "password" : "pass"
        }
    },
    "response": {
        "status": 200
    }
}
```

###JSONPath examples:

Request example:

```json
{
	"user" : {
		"name" : "John",
		"lastname" : "Smith",
		"familyMembers" : ["mother", "father", "sister"]
	}
}
```

WireMock mapping:

```json
{
	"request" : {
		"bodyPatterns" : [
			{ "matchesJsonPath": "$.user[?(@.name == 'John')]" }, 
			{ "matchesJsonPath": "$.user[?(@.lastname =~ /Smi.*/i)]"},
			{ "matchesJsonPath": "$.user[?(@.familyMembers.size() == 3)]"}
		]
	}
}
```

#RESPONSE

###Normal example:

```json
{
	"response": {
		"body" : "Hello world!"
	}
}
```

###Body in file example:

```json
{
	"response": {
		"bodyFileName" : "files/example.html",
		"bodyFileName" : "files/example.json"
	}
}
```

#RESPONSE TEMPLATING

Templates have to be enabled with either `--global-response-templating` or  `--local-response-templating` before being able to use them in the standalone version.

###Get data from request:

```json
{
	"response" : {
		"body" : "{{request.path.[0]}}"
	}
}
```

###Extracting values from JSON:

Example request body:

```json
"body": {
	"user" : {
		"name" : "John",
		"lastname" : "Smith",
		"familyMembers" : ["mother", "father", "sister"]
	}
}
```

This this will render `John`:

```json
{
	"response" : {
		"body" : "{{jsonPath request.body '$.user.name'}}"
	}
}
```

And this will render `["mother", "father", "sister"]` because it conserves JSON syntax:

```json
{
	"response" : {
		"body" : "{{jsonPath request.body '$.user.familyMembers'}}"
	}
}
```