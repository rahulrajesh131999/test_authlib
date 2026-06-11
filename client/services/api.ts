const BASE_URL = "http://localhost:8000/api/v1"

// auth endpoints

export const endpoints = {
    REGISTER_API : BASE_URL + "/auth/register",
    LOGIN_API : BASE_URL + "/auth/login",
    ME_API: BASE_URL + "/auth/me",
    LOGOUT_API : BASE_URL + "/auth/logout",
}