import { endpoints } from "../api";


const {LOGIN_API, REGISTER_API, ME_API} = endpoints;

interface LoginData {
    email : string,
    password : string,
}

interface ReginsterData extends LoginData {
    fullName : string,
    confirmPassword : string
}

export const registerapi = async (data:ReginsterData) =>{
    const {fullName, email, password, confirmPassword} = data;

    try {
        const response = await fetch(REGISTER_API,{
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({
                full_name : fullName,
                email : email,
                password : password,
                confirm_password : confirmPassword
            }),
            credentials:"include"
        })

        if(!response.ok){
            throw Error("Request failed")
        }

        const data = await response.json()

        console.log("printing user details: ",data)

        return data
    } catch (error) {
        console.error("REGISTER API ERROR.........", error)
    }
}


export const loginapi = async(data:LoginData) =>{

    const {email, password} = data;

    try {
        const response = await fetch(LOGIN_API,{
            method: "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({
                email : email,
                password : password
            }),
            credentials : "include"
        })

        if(!response.ok){
            throw Error("failed to login")
        }

        const data = await response.json()
        console.log("printing user details: ",data)
        return data

    } catch (error) {
        console.error("LOGIN API ERROR.........", error)
    }
}
