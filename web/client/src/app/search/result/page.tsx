import Loading from "@/app/finder/result/loading"
import Link from "next/link"
import { Suspense } from "react"

type FinderSearchParams = {
  key1: string
  key2: string
  key3: string
  search: string
  d: string
  p: string
}

async function getDateByKeywords(
  key: string[],
  search: string,
  d: string,
  p: string
) {
  const body = {
    url: search,
    keywords: key,
    d: 2,
    p: 1,
  }

  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/v1/crawl/generate_html`,
      {
        method: "POST",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      }
    )
    const data = await response.json()
    return data
  } catch (error) {}
}

export default async function FinderResult({
  searchParams,
}: {
  searchParams: FinderSearchParams
}) {
  const { key1, key2, key3, search, d, p } = searchParams

  const keys: string[] = []

  if (key1) {
    keys.push(key1)
  }
  if (key2) {
    keys.push(key2)
  }
  if (key3) {
    keys.push(key3)
  }

  console.log(keys)

  const keywords = await getDateByKeywords(keys, search, d, p)
  console.log(keywords)

  return (
    <section className="grid gap-8 container my-8 animate-pulse">
      <div className="h-6 bg-gray-200 rounded w-1/2 mx-auto"></div>
      <div className="h-4 bg-gray-200 rounded w-1/4 mx-auto"></div>
      <div className="grid gap-4">
        <div className="h-4 bg-gray-200 rounded w-1/3 mx-auto"></div>
        <div className="flex border rounded-md border-white px-4 py-4 flex-col gap-2">
          <div className="h-4 bg-gray-200 rounded w-full"></div>
          <div className="h-4 bg-gray-200 rounded w-full"></div>
          <div className="h-4 bg-gray-200 rounded w-1/2"></div>
        </div>
        <div className="h-4 bg-gray-200 rounded w-1/4 mx-auto"></div>
      </div>

      <div className="grid gap-4">
        <div className="h-4 bg-gray-200 rounded w-1/3 mx-auto"></div>
        <div className="flex border rounded-md border-white px-4 py-2 flex-col gap-2">
          <div className="h-4 bg-gray-200 rounded w-full"></div>
          <div className="h-4 bg-gray-200 rounded w-1/2"></div>
        </div>
        <div className="h-4 bg-gray-200 rounded w-1/4 mx-auto"></div>
      </div>

      <p className="text-center">Data is being collected...</p>
      <p className="text-center text-xl">
        Fetching links, downloading html files matching the keyword...
      </p>
    </section>
  )
}
