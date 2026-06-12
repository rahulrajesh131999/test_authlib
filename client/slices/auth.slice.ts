import {createSlice} from "@reduxjs/toolkit"
import type {PayloadAction} from "@reduxjs/toolkit"
import type {RootState} from "@/reducer/index"

interface Auth {
    userId : string | null ,
    loading : boolean
}

const initialState : Auth = {
    userId : null,
    loading : true
}

export const authSlice = createSlice({
    name : "auth",
    initialState : initialState,
    reducers : {
        setUser:(state,action)=>{
            state.userId = action.payload
            state.loading = false
        },
        clearUser : (state) =>{
            state.userId = null
            state.loading = false
        },
        setLoading : (state, action) =>{
            state.loading = action.payload
        }
    }
})

export const {setUser, clearUser, setLoading} = authSlice.actions

export const selectAuth =(state: RootState) => state.auth

export default authSlice.reducer