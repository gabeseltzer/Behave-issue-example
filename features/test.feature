Feature: Test

    @fixture.withServer("Version123")
    Scenario: Test without outline
        Given a thing
        When nothing
        Then nothing


    @fixture.withServer("Version123")
    Scenario Outline: Test with outline
        Given a thing
        When "<something-interesting>" is printed
        Then nothing

        Examples: Some examples
            | something-interesting | 
            | thing one             |
            | thing 2               |