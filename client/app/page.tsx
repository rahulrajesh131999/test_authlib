
import Registerform from '@/components/auth/Registerform'
import React from 'react'
import Image from 'next/image'
import stockImage from "@/assets/images/antipolygon-youtube-l6SwTEW2i9I-unsplash.jpg"
import UseAuthInit from '@/hooks/UseAuthInit'

const app = () => {
  //UseAuthInit()
  return (
    <div className='flex lg:justify-between gap-10 my-10 lg:my-0 min-h-screen lg:items-center justify-center items-center'>
      <div className="w-100">
        <Registerform/>
      </div>
      <div className='relative hidden w-150 h-150 lg:block overflow-hidden'>
        <Image alt='image' src={stockImage} fill className='w-full h-full object-cover rounded-md'/>
      </div>
    </div>
  )
}

export default app