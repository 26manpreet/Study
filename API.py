SERVICE     -> is some code or function , which can be used for ACTION or SHARE DATA across web service

WEBSERVICE  ->  service accessed over web .e.g, WeatherService , OrderService 


                |------|   --Request----->  |------|            
                |Client|                    |Server|            
                |------|  <---Response----  |------|            




#-------------------------------------------
# API (Application Programming interface)
#-------------------------------------------
    - Webservice that allows to application to interact with each other 
    - Multiple API's can exist on webserver and each API has its own ENDPOINT.


                |------|  -----------Request--------> |A|       |------|            ----------
                |Client|                              |P| <---> |Server| <-------> | database |
                |------|  <--------Response---------- |I|       |------|            ----------
                        (Response code + Response Data)

                                                    ------------------------------------------------------                        
                                                    | API Authorisation Server (optional for TOken based) |
                                                    ------------------------------------------------------
            Paylaod - Body of Request or Response
                                                    

    # Response codes  ( same as HTTP error codes)
    
        1XX( informational)
        
        2XX (Successful)
        200 - OK            : Request was successfulesuccess
        202 -               : Request created ( POST )
        204 - No Content    : Request was successful, but resource didnt return any data
        
        3XX ( redirectional)
        
        4XX (Client error)
        400 - bad request   : incorrect request format
        401 - unauthorised  : 
        403 - forbidden     : Access to resource is denied
        404 - Non found     : Requested resource not found

        5XX (Server Error)
        503 - service unavailable

    
    #----------------
    #WHY API ??
    #----------------
        - REAL TIME DATA    - as its changes frequently and its difficult to download file everytime
        - Light implementation and different technolgies can interact in standard way
        - Provides ease of flexibility to use application  - Suppose , you need to book a movie Ticket  
                                                                Legacy approach :
                                                                    1. Go to Theatre
                                                                    2. Pay and Book ticket , only authorised staff can book 
                                                                API :
                                                                    Do everything from home 


            #Real Time Eamples : 
                Movies - Ticket booking  , Seat availablilty , Pictures , Show timings
                Bank   - Account Balance check and Money transfer etc    



    #-------------------
    # Major API requests ( CRUD):
    #-------------------
        - GET               - Read    # recieves data 
        - PUT               - update  # share data (in xml/json) to update
        - POST              - create  # share data to add 
        - DELETE            - Delete  # share data (in xml/json) to update



    #-------------------
    # Token Based API:
    #-------------------
   
   ---------                                     ----------------------------                       
   |       |                                     |                          |
   | Client|--------------Request--------------->| Authorisation API Server |
   |       |<----------Access Token--------------|                          |
   ---------                                     ----------------------------   
   
   
        Authentication 
            1. Client requests to API , verifies access and issues Token to client (for authorisation after verifying authentication)
        Authorisation
            2. Token is further used to access resources


    #--------------------------------------------------
    # Different ways of authentication in API:
    #--------------------------------------------------
        1. HTTP Basic Authenticaton - username/passwd is sent along every API call  ( Simple )
        2. API Key Authentication   - A Secret key is generated for user, which is used for every call ( AWS )
        3. OAUTH Authentication     - combination of authentication+authorisation , when user request , after verfying authentication ,token is issued for authorisation .( Mostly used, most secure ,                              TOKEN BASED)





#-------------------------------------------
# REST API ( Representational State Transfer)
#-------------------------------------------
    - Its is an architectural style for API 
    - API that follow all REST constraints is called RESTful service/API


                        URL + Method + Reuest Header(credentials etc) + Body ( not for GET)
                |------|  -----------Request------------------------------------> |A|       |------|            ----------
                |Client|                                                          |P| <---> |Server| <-------> | database |
                |------|  <--------Response----------------------------           |I|       |------|            ----------
                        (Response code + Response Header + Resource(data))




    #-----------------------------------------
    # REST API architectural constraints:
    #-----------------------------------------
            1. Uniform interface : API must have uniform interface, so that each api at client side use it consistently.
            2. Client–server     : client serve may be alteres at each side untill interface is uniform
            3. Stateless         : client needs to always request for resource , as server dont store previous state
            4. Cacheable         : Cacheable layer to improve performance ( client <--> cache <--> server)
            5. Layered system    : REST allows to use layered architecter - API can exist on Server A, database on Server B and authenticater Server C. Or, additional layer of load balancer
            6. Code on demand (optional) : allows to download executable code from server and runs on client

    - Mostly data is in JSON/XML format
    - REST API treats any data (image/video/text) as resource that can have CRUD operations
    - REST API is STATELESS, means one request is not dependent on any other requests i.e., servers only knows about current request not previous.
        e.g, if one user hit endpoint in first request and again hits then each time proper params and credentials need to be provided.




    #-------------------------
    # Types of API's:
    #-------------------------
    # ----------------------------------------------------------------------------------------------------------
    #   1. RESTful API ( mostly used)                  vs                     2. SOAP
    # ----------------------------------------------------------------------------------------------------------
    - Representational State Transfer                               - Simple Object Access Protocol
    - Supports - text, XML, HTML: and JSON                         - only XML
    - Low bandwidth required for requests                           - more bandwidth required , as they include other details too
    - REST can use SOAP                                             - cant use REST




- API testing is achieved using Postman


- RESTful API uses URL ( uniform resource locator) - to locate resource
        
        http:// < host > / <path> [ ? Query]

        e.g, https: //Google.com/API/Map?location=Delhi

            Https       - Protocol
            Google.com  - host
            API/MAP     - path
            Query       - Location=Delhi


- curl <endpoint>




#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------

Modules avalailable in python
- urllib/urllib2
- httplib
- requests  (mostly used of being simplest , more feature, session object, no manual encoding required) 




#--------------------
#--simple api call
#--------------------
    import requests
    import json

    response=requests.get('https://api.exchangeratesapi.io/latest')

    if response.status_code==200:
        print(response.text)   # Payload in string bytes
        print('*'*50)
        print(response.json())  #diff bw json() and text is that json()-->has key '' properly while text has key ""
        print('*'*50)
        print(json.loads(response.text)) #convert string into json , same as response.json()
    else:
        print('error while retreiving data')


    #---------------------------
    # POST Request
    #---------------------------
    payload = { user : 'Money' , City : 'Delhi'}
    response=requests.get('https://api.exchangeratesapi.io/latest' , data=payload)


#-------------------------------------------
#--with parameters only required one
#-------------------------------------------
    import requests

    #https://api.exchangeratesapi.io/latest?base=USD

    response=requests.get('https://api.exchangeratesapi.io/latest',params={'base':'USD'})  #above URL can also be used directly
    if response.status_code==200:
        print(response.text)
    else:
        print('error while retreiving data')


#-------------------------------------------
#---write currency conversion program.
#-------------------------------------------



#-------------------------------------------
#-------with Authentication
#-------------------------------------------
    from requests.auth import HTTPBasicAuth

    requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))