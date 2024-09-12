# ClientDetailsObject

Describes the fields in the client_details object in REST messages for payments. The client_details object describes the browser that the customer is using. The client collects this information and sends it as part of the Create Payment request. This information is used for processing the 3DS version 2 authentication of the customer. Note that Client Details information is not returned in the API response and it does not appear in any webhooks.

**Properties**

| Name                | Type               | Required | Description                                                                                   |
| :------------------ | :----------------- | :------- | :-------------------------------------------------------------------------------------------- |
| ip_address          | `str`              | ❌       | IP address of the customer.                                                                   |
| java_enabled        | `bool`             | ❌       | Indicates whether the browser is enabled for Java.                                            |
| java_script_enabled | `bool`             | ❌       | Indicates whether the browser is enabled for JavaScript.                                      |
| language            | `str`              | ❌       | The language the browser is configured for, as defined in IETF BCP 47.                        |
| screen_color_depth  | `ScreenColorDepth` | ❌       | Indicates the screen color depth of the customer's browser, in bits.                          |
| screen_height       | `int`              | ❌       | Height of the customer's screen, in pixels. 1-6 digits.                                       |
| screen_width        | `int`              | ❌       | Width of the customer's screen, in pixels. 1-6 digits.                                        |
| time_zone_offset    | `int`              | ❌       | Difference in minutes between UTC and the customer's time zone. Positive or negative integer. |

# ScreenColorDepth

Indicates the screen color depth of the customer's browser, in bits.

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| \_1  | `int` | ✅       | 1           |
| \_4  | `int` | ✅       | 4           |
| \_8  | `int` | ✅       | 8           |
| \_15 | `int` | ✅       | 15          |
| \_16 | `int` | ✅       | 16          |
| \_24 | `int` | ✅       | 24          |
| \_32 | `int` | ✅       | 32          |
| \_48 | `int` | ✅       | 48          |
