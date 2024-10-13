# VerifyService

A list of all methods in the `VerifyService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                     | Description                                                                                                                                                                                                                                                                        |
| :------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_v1_identities](#create_v1_identities)                                               | Verification of the identity of a personal contact associated with a wallet.                                                                                                                                                                                                       |
| [get_kyc_id_verification_supported_doc_types](#get_kyc_id_verification_supported_doc_types) | Use this method to determine the types of documents to use for identification purposes, and also whether you need the reverse side of the document. You can filter your search results by country with the country query parameter.                                                |
| [get_application_types_by_country](#get_application_types_by_country)                       | Retrieve a List types of identity verification applications by country. You can filter the list with query parameters.                                                                                                                                                             |
| [get_application_status](#get_application_status)                                           | Retrieve the status of an application for verification of identity. You can filter the list with query parameters.                                                                                                                                                                 |
| [create_hosted_application_token](#create_hosted_application_token)                         | Create an application for Rapyd Verify where the client (applicant) provides information directly to Rapyd. After the applicant submits the application on the hosted page, Rapyd verifies the information. When the status of the application changes, Rapyd sends you a webhook. |
| [get_hosted_application_by_token](#get_hosted_application_by_token)                         | Retrieve Rapyd Verify Application                                                                                                                                                                                                                                                  |

## create_v1_identities

Verification of the identity of a personal contact associated with a wallet.

- HTTP Method: `POST`
- Endpoint: `/v1/identities`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [V1IdentitiesBody](../models/V1IdentitiesBody.md) | ✅       | The request body. |

**Return Type**

`InlineResponse200_85`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import V1IdentitiesBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = V1IdentitiesBody(
    back_side_image="back_side_image",
    back_side_image_mime_type="back_side_image_mime_type",
    contact="contact",
    country="GB",
    document_type="document_type",
    ewallet="ewallet",
    face_image="face_image",
    face_image_mime_type="face_image_mime_type",
    front_side_image="front_side_image",
    front_side_image_mime_type="front_side_image_mime_type",
    reference_id="reference_id",
    request_type="request_type",
    send_callback="send_callback"
)

result = sdk.verify.create_v1_identities(request_body=request_body)

print(result)
```

## get_kyc_id_verification_supported_doc_types

Use this method to determine the types of documents to use for identification purposes, and also whether you need the reverse side of the document. You can filter your search results by country with the country query parameter.

- HTTP Method: `GET`
- Endpoint: `/v1/identities/types`

**Parameters**

| Name    | Type | Required | Description                                                    |
| :------ | :--- | :------- | :------------------------------------------------------------- |
| country | str  | ✅       | Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase. |

**Return Type**

`InlineResponse200_86`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.verify.get_kyc_id_verification_supported_doc_types(country="GB")

print(result)
```

## get_application_types_by_country

Retrieve a List types of identity verification applications by country. You can filter the list with query parameters.

- HTTP Method: `GET`
- Endpoint: `/v1/verify/applications/types/country/{country}`

**Parameters**

| Name    | Type | Required | Description                                                    |
| :------ | :--- | :------- | :------------------------------------------------------------- |
| country | str  | ✅       | Two-letter ISO 3166-1 ALPHA-2 code for the country. Uppercase. |

**Return Type**

`InlineResponse200_87`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.verify.get_application_types_by_country(country="GB")

print(result)
```

## get_application_status

Retrieve the status of an application for verification of identity. You can filter the list with query parameters.

- HTTP Method: `GET`
- Endpoint: `/v1/verify/applications/status/{application}`

**Parameters**

| Name        | Type | Required | Description                                        |
| :---------- | :--- | :------- | :------------------------------------------------- |
| application | str  | ✅       | ID of the application. String starting with app\_. |

**Return Type**

`InlineResponse200_88`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.verify.get_application_status(application="application")

print(result)
```

## create_hosted_application_token

Create an application for Rapyd Verify where the client (applicant) provides information directly to Rapyd. After the applicant submits the application on the hosted page, Rapyd verifies the information. When the status of the application changes, Rapyd sends you a webhook.

- HTTP Method: `POST`
- Endpoint: `/v1/verify/applications/hosted`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ApplicationsHostedBody](../models/ApplicationsHostedBody.md) | ❌       | The request body. |

**Return Type**

`InlineResponse200_89`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment
from rapyd_sdk.models import ApplicationsHostedBody

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ApplicationsHostedBody(
    application_type="application_type",
    country="country",
    rapyd_entity_token="ewallet_ef84c580177dbfc4293b1cf73c73fc77",
    phone_number="phone_number",
    metadata={},
    client_reference_id="client_reference_id",
    cancel_url="cancel_url",
    complete_url="complete_url"
)

result = sdk.verify.create_hosted_application_token(request_body=request_body)

print(result)
```

## get_hosted_application_by_token

Retrieve Rapyd Verify Application

- HTTP Method: `GET`
- Endpoint: `/v1/verify/applications/hosted/{verifyAppId}`

**Parameters**

| Name          | Type | Required | Description                                                      |
| :------------ | :--- | :------- | :--------------------------------------------------------------- |
| verify_app_id | str  | ✅       | ID of the Rapyd Verify application. String starting with happ\_. |

**Return Type**

`InlineResponse200_90`

**Example Usage Code Snippet**

```python
from rapyd_sdk import RapydSdk, Environment

sdk = RapydSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.verify.get_hosted_application_by_token(verify_app_id="verifyAppId")

print(result)
```
