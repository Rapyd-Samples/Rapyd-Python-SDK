# NextAction

Indicates the next action for completing the payment. Response only. One of the following values are - _ 3d_verification - The next action is 3DS authentication. To simulate 3DS authentication in the sandbox, see Simulating 3DS Authentication. Relevant only to card payments. _ pending_capture - The next action is pending the capture of the amount. Relevant only to card payments when the amount is not zero. _ pending_confirmation - The next action is pending the confirmation for the payment. Relevant to all payment methods excluding card payment. _ not_applicable - The payment has completed or the next action is not relevant.

**Properties**

| Name                | Type  | Required | Description            |
| :------------------ | :---- | :------- | :--------------------- |
| \_3DVERIFICATION    | `str` | ✅       | "3d_verification"      |
| PENDINGCAPTURE      | `str` | ✅       | "pending_capture"      |
| PENDINGCONFIRMATION | `str` | ✅       | "pending_confirmation" |
| NOTAPPLICABLE       | `str` | ✅       | "not_applicable"       |
