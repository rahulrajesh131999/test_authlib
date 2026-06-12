import {NextResponse} from "next/server"
import type{NextRequest} from "next/server"

export function middleware(req:NextRequest){

    const token = req.cookies.get("access_token")

    const pathname = req.nextUrl.pathname

    const protectedRoute = ["/dashboard"]

    const isPublic =
  pathname === "/" ||
  pathname === "/login"

    const isProtected = protectedRoute.some((route)=>{
        return req.nextUrl.pathname.startsWith(route)
    })

    if(isProtected && !token){
        return NextResponse.redirect(new URL("/", req.url))
    }

    if(token && isPublic){
        return NextResponse.redirect(new URL("/dashboard", req.url))
    }

    return NextResponse.next()
}

export const config = {
  matcher: ["/dashboard/:path*", "/", "/login"],
};