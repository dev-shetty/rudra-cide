"use client"

import Loading from "@/app/finder/result/loading"
import { Suspense, useEffect, useState } from "react"

export default function FinderResult() {
  const [loading, setLoading] = useState(true)
  // Simulate loading for 3 seconds
  useEffect(() => {
    const timer = setTimeout(() => {
      setLoading(false)
    }, 3000)

    // Clear timeout on component unmount to avoid memory leaks
    return () => clearTimeout(timer)
  }, [])
  return (
    <Suspense fallback={<Loading />}>{!loading && <div>Hello</div>}</Suspense>
  )
}
