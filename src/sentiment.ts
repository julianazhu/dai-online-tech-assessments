export interface Event {
  customerId: string
  callId: number
  sentiments: string[]
}

export const topSentiments = (events: Event[], topN: number, customerId: string): string[] => {

  throw new Error("not Implemented")

}
