const axios = require('axios');
jest.mock('axios');

describe('/lyrics/{songID} endpoint', () => {
  test('GET /lyrics/{songID} with a valid songID should return status code 200 and a lyrics object', async () => {
    // Assuming '1' is a valid songID for testing purposes
    const songID = '1';
    const mockLyrics = {
      lyrics: 'We were both young when I first saw you...'
    };

    jest.spyOn(axios, 'get').mockResolvedValue({
      status: 200,
      data: mockLyrics
    });

    const response = await axios.get(`https://taylor-swift-api.sarbo.workers.dev/lyrics/${songID}`);
    expect(response.status).toBe(200);
    expect(response.data).toHaveProperty('lyrics');
    expect(typeof response.data.lyrics).toBe('string');
  });

  // Additional tests for other scenarios like invalid songID, server errors, etc., can be added here
});
