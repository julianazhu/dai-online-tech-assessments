export interface Event {
  customerId: string
  callId: number
  sentiments: string[]
}

/**
 * @returns the top_n sentiments of a customer from call events
 * @param events - List of call events
 * @example
 * ```ts
 * [
 *  {
 *    customerId: 'a',
 *    callId: 1,
 *    sentiments: ['happy', 'sad', 'bored']
 *  }
 * ]
 * ```
 * @param topN - number of sentiments to return
 * @param customerId - The string of customer id
 *
 */
export const topSentiments = (events: Event[], topN: number, customerId: string): string[] => {

  throw new Error("not Implemented")

}
