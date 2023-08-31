import { fakeFetchDataById } from "../fakeFetch";
import type { fakeDataType } from "../fakeFetch";
import { useQuery } from "react-query";

export default function useFakeDataById(id: number) {
    return useQuery<fakeDataType>({
        queryKey: ["fakeData", id],
        queryFn: () => fakeFetchDataById(id),
        retry: false,
    })
}