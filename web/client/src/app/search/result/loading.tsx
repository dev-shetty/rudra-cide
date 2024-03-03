export default function Loading() {
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

      <p className="text-center">Wait till we crawl the web for you...</p>
    </section>
  )
}
