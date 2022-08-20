#!/usr/bin/env python3

def name():
    """
    Provides my full name.
    
    :return: My full name 
    :rtype: str
    """
    return("Samuel Mehalko")

def title():
    """
    Provides my title at the company that I am employeed.
    
    :return: My title
    :rtype: str
    """
    return("Embedded Software Engineer")

def company():
    """
    Provides the name of the company that I am employeed.
    
    :return: My company
    :rtype: str
    """
    return("Northrop Grumman Corporation")

def email():
    """
    Provides my office email address.
    
    :return: My email address 
    :rtype: str
    """
    return("samuel.mehalko@ngc.com")

def phone():
    """
    Provides my office phone number.
    
    :return: My phone number 
    :rtype: str
    """
    return("(410)-993-6848")

def site():
    """
    Provides the url of the associated github pages website.
    
    :return: The associated github page's url
    :rtype: str
    """
    return("https://pypi.org/project/contact_sam")

def package():
    """
    Provides the url of the this package on the Python Package Index (pypi) website.
    
    :return: This package's pypi url
    :rtype: str
    """
    return("https://pypi.org/project/contact_sam")


def source():
    """
    Provides the url of the this package's source github url.
    
    :return: This source code's github url.
    :rtype: str
    """
    return("https://github.com/contact-sam/contact_sam")

def main():
    """
    Provides a short blurb of of my contact information as well as some fun links.
    
    :return: My contact information as well as some fun links.
    :rtype: str
    """
    print(f"""
    Hi, my name is {name()}!
    I am an {title()}
    working for {company()}.
    I can be reached via email (preferred) at {email()}
    or via phone at {phone()}.

    The python package used to generate this text can be found at {site()}
    and the source can be found at {source()}
    """)

if __name__ == "__main__":
    main()
