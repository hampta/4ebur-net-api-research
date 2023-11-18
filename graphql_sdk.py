from enum import Enum


class SDK(Enum):
    select_domain_response_fragment = """fragment SelectDomainResponse on SelectDomainOutput {
                        success
                        error
                        domain {
                            id
                            name
                        }
                    } """

    too_many_requests_response_fragment = """ fragment TooManyRequestsResponse on TooManyRequestsException {
                        success
                        tooManyRequestsExceptionError: error
                    } """

    unauthorized_response_fragment = """ fragment UnauthorizedResponse on UnauthorizedException {
                        success
                        unauthorizedExceptionError: error
                    } """

    forbidden_response_fragment = """ fragment ForbiddenResponse on ForbiddenException {
                        success
                        forbiddenExceptionError: error
                    } """

    select_node_response_fragment = """fragment SelectNodeResponse on SelectNodeOutput {
                        success
                        selectNodeOutputError: error
                        node {
                            regionCode
                            countryAlpha2
                            serverProtocol
                            serverHost
                            data
                        }
                    }"""

    get_purchases_response_fragment = """fragment GetPurchasesResponse on GetPurchasesOutput {
                    success
                    purchases {
                        status
                        type
                        purchaseDetailsSubscription {
                            expirableAt
                            type
                        }
                    }
                }"""

    register_user_response_fragment = """fragment RegisterUserResponse on RegisterUserOutput {
                        success
                        licenseKey
                    }"""

    login_user_response_fragment = """fragment LoginUserResponse on LoginUserOutput {
                        success
                        error
                        accessToken
                        refreshToken
                    }"""

    subscription_response_fragment = """fragment SubscriptionResponse on SubscriptionData {
                        expirableAt
                    }"""

    get_purchases_response = """fragment GetPurchasesResponse on GetPurchasesOutput {
                    success
                    purchases {
                        status
                        type
                        purchaseDetailsSubscription {
                            expirableAt
                            type
                        }
                    }
                }"""

    subscription_data_response_fragment = """ fragment SubscriptionDataResponse on SubscriptionData {
                        expirableAt
                    } """

    get_users_response_fragment = """fragment GetUserResponse on GetUserOutput {
                    success
                    user {
                        licenseKey
                        email
                    }
                    userRiskLevelType
                    permissionsSummary {
                        ACTIVE_SUBSCRIPTION {
                            permitted
                            data {
                                __typename
                                ...SubscriptionDataResponse
                            }
                        }
                    }
                }""" \
                + subscription_data_response_fragment

    request_otp_response_fragment = """fragment RequestOtpResponse on RequestOtpOutput {
                    success
                    error
                }"""

    create_otp_response_fragment = """fragment CreateOtpResponse on CreateOtpOutput {
                    success
                    error
                }"""

    restore_user_response_fragment = """fragment RestoreUserResponse on RestoreUserOutput {
                    success
                    error
                }"""

    set_email_response_fragment = """fragment SetEmailResponse on SetEmailOutput {
                    success
                    error
                }"""

    get_zones_response_fragment = """fragment GetZonesResponse on GetZonesOutput {
                        success
                        zones {
                            regionId
                            regionCode
                            countryAlpha2
                            serverProtocol
                            serverHost
                            regionName
                            nodeIsAvailable
                            serverType
                            nodeEfficiency
                            nodeWorkload
                        }
                    }"""

    select_domain_document = """query SelectDomain {
                    selectDomain {
                        __typename
                        ...SelectDomainResponse
                        ...TooManyRequestsResponse
                        ...UnauthorizedResponse
                    }
                } """ \
                    + select_domain_response_fragment \
                    + too_many_requests_response_fragment \
                    + unauthorized_response_fragment

    get_languages_document = """query GetLanguages {
                    getLanguages {
                        success
                        languages {
                            alpha2
                            alpha3
                            id
                            name
                            deletedAt
                        }
                    }
                }"""

    select_node_document = """query SelectNode($payload: SelectNodeInput!) {
                    selectNode(payload: $payload) {
                        __typename
                        ...SelectNodeResponse
                        ...TooManyRequestsResponse
                        ...UnauthorizedResponse
                    }
                }""" \
                    + select_node_response_fragment \
                    + too_many_requests_response_fragment \
                    + unauthorized_response_fragment \


    get_purchases_document = """query GetPurchases {
                    getPurchases {
                        __typename
                        ...GetPurchasesResponse
                        ...UnauthorizedResponse
                    }
                }""" \
                    + get_purchases_response_fragment \
                    + unauthorized_response_fragment

    register_user_document = """mutation RegisterUser {
                    registerUser {
                        __typename
                        ...RegisterUserResponse
                        ...TooManyRequestsResponse
                    }
                }""" \
                    + register_user_response_fragment \
                    + too_many_requests_response_fragment

    login_user_document = """mutation LoginUser($payload: LoginUserInput!) {
                    loginUser(payload: $payload) {
                        __typename
                        ...LoginUserResponse
                        ...TooManyRequestsResponse
                    }
                }""" \
                    + login_user_response_fragment \
                    + too_many_requests_response_fragment

    refresh_token_document = """mutation RefreshToken($payload: RefreshTokenInput!) {
                    refreshToken(payload: $payload) {
                        success
                        error
                        accessToken
                        refreshToken
                    }
                }"""

    get_users_document = """query GetUsers {
                    getUsers {
                        __typename
                        ...GetUserResponse
                        ...UnauthorizedResponse
                    }
                }""" \
                    + get_users_response_fragment \
                    + unauthorized_response_fragment

    use_otp_document = """mutation UseOtp($payload: UseOtpInput!) {
                    useOtp(payload: $payload) {
                        __typename
                        ...RequestOtpResponse
                    }
                }""" \
                    + request_otp_response_fragment \


    request_otp_document = """mutation RequestOtp {
                    requestOtp {
                        __typename
                        ...RequestOtpResponse
                    }
                }""" \
                    + request_otp_response_fragment \


    create_otp_document = """mutation CreateOtp {
                    createOtp {
                        __typename
                        ...CreateOtpResponse
                        ...UnauthorizedResponse
                    }
                }""" \
                    + create_otp_response_fragment \
                    + unauthorized_response_fragment

    restore_user_document = """query RestoreUser($payload: RestoreUserInput!) {
                    restoreUser(payload: $payload) {
                        __typename
                        ...RestoreUserResponse
                        ...TooManyRequestsResponse
                    }
                }""" \
                    + restore_user_response_fragment \
                    + too_many_requests_response_fragment

    set_email_document = """mutation SetEmail($payload: SetEmailInput!) {
                    setEmail(payload: $payload) {
                        __typename
                        ...SetEmailResponse
                        ...TooManyRequestsResponse
                        ...UnauthorizedResponse
                    }
                }""" \
                    + set_email_response_fragment \
                    + too_many_requests_response_fragment \
                    + unauthorized_response_fragment

    get_zones_document = """query GetZones {
                    getZones {
                        __typename
                        ...GetZonesResponse
                        ...UnauthorizedResponse
                    }
                }""" \
                    + get_zones_response_fragment \
                    + unauthorized_response_fragment
