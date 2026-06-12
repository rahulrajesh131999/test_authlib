"use client"
import { useAppDispatch } from '@/reducer/reducerHooks'
import { clearUser, setLoading, setUser } from '@/slices/auth.slice'
import React, { useEffect } from 'react'
import {endpoints} from "@/services/api"

const UseAuthInit = () => {

    const dispatch = useAppDispatch()

    useEffect(()=>{
        const authInit=async()=>{
            try {
                dispatch(setLoading(true))
            const res = await fetch(endpoints.ME_API,{
                method : "GET",
                credentials : "include"
            })
            if(!res.ok){
                throw new Error("not authenticated")
            }
            const data = await res.json()
            dispatch(setUser(data.user))
            // console.log("user details from auth init: ", data.user.id)
            dispatch(setLoading(false))
            } catch (error) {
                console.error(error)
                dispatch(clearUser())
            }     
        }
        authInit()

    },[dispatch]);
    return null
}

export default UseAuthInit