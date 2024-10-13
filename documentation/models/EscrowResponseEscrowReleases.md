# EscrowResponseEscrowReleases

Array of objects that describe individual releases.

**Properties**

| Name        | Type                             | Required | Description                                                                                       |
| :---------- | :------------------------------- | :------- | :------------------------------------------------------------------------------------------------ |
| data        | EscrowResponseEscrowReleasesData | ❌       | Array of objects that describe individual escrow releases.                                        |
| has_more    | bool                             | ❌       | Indicates that the number of escrow releases is greater than the number returned in the response. |
| total_count | float                            | ❌       | Number of escrow releases.                                                                        |
| url         | str                              | ❌       | URL for the record of all escrow releases for this payment.                                       |
