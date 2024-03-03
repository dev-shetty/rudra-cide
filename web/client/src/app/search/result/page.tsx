import Loading from "@/app/finder/result/loading"
import Link from "next/link"
import { Suspense } from "react"

type FinderSearchParams = {
  key1: string
  key2: string
  key3: string
  search: string
}

async function getUserAlias(key: string[], search: string) {
  const body = {
    search,
    key,
  }

  const response = await fetch(
    `${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/v1/alias/alias-user`,
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
}

export default async function FinderResult({
  searchParams,
}: {
  searchParams: FinderSearchParams
}) {
  const { key1, key2, key3, search } = searchParams
  console.log({ key1, key2, key3, search })

  const keys = [key1, key2, key3]
  console.log(keys)

  //   const userAlias = await getUserAlias(key, search)
  //   console.log(userAlias)

  return (
    <Suspense fallback={<Loading />}>
      <section className="grid gap-8 container my-8">
        {/* <h1 className="text-center my-4 text-2xl">
          Reddit search for User: {username} and Keyword: {key}
        </h1>
        <div className="grid gap-4">
          <h2 className="text-xl px-4">
            Posts where {username} mentioned <b>&quot;{key}&quot;</b>:{" "}
          </h2>
          {userAlias.data.posts.map((post: any, index: number) => (
            <div
              key={post.url}
              className="flex border rounded-md border-white px-4 py-4 flex-col gap-2"
            >
              <p className="text-lg font-bold">{post.title}</p>
              <p>{post.text}</p>
              <p>
                Post url:{" "}
                <Link href={post.url} className="underline text-blue-200">
                  {post.url}
                </Link>
              </p>
            </div>
          ))}

          {userAlias.data.posts.length === 0 ? (
            <p className="ml-2">No posts available</p>
          ) : (
            ""
          )}
        </div>

        <div className="grid gap-4">
          <h2 className="text-xl px-4">
            Comments where {username} mentioned <b>{key}</b>:{" "}
          </h2>
          {userAlias.data.comments.map((comment: any, index: number) => (
            <div
              key={comment.url}
              className="flex border rounded-md border-white px-4 py-2 flex-col gap-2"
            >
              <p>{comment.text}</p>
              <p>
                Comment url:{" "}
                <Link href={comment.url} className="underline text-blue-200">
                  {comment.url}
                </Link>
              </p>
            </div>
          ))}
          {userAlias.data.comments.length === 0 ? (
            <p className="ml-2">No comments available</p>
          ) : (
            ""
          )}
        </div> */}
      </section>
    </Suspense>
  )
}
