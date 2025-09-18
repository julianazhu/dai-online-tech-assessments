import { topSentiments, Event } from './sentiment'

describe('topSentiments', () => {

  it('run first test', () => {
    const events: Event[] = [
      {customerId: 'a', callId: 1, sentiments: ['happy', 'sad', 'bored']},
      {customerId: 'a', callId: 2, sentiments: ['happy', 'bored', 'sleepy']},
      {customerId: 'a', callId: 3, sentiments: ['doubtful', 'happy']},
      {customerId: 'b', callId: 4, sentiments: ['bored']},
    ]

    // TBD
  })

})

