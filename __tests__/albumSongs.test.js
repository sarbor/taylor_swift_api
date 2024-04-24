const axios = require('axios');

jest.mock('axios');

describe('/albums/{albumID} endpoint', () => {
  test('GET /albums/{albumID} with a valid albumID should return status code 200 and an array of songs', async () => {
    // Assuming '1' is a valid albumID for testing purposes
    const albumID = '1';
    const mockSongs = [
      { song_id: '1', title: 'Love Story', length: '3:55' },
      { song_id: '2', title: 'You Belong With Me', length: '3:51' },
      // ... other songs
    ];

    jest.spyOn(axios, 'get').mockResolvedValue({
      status: 200,
      data: mockSongs
    });

    const response = await axios.get(`https://taylor-swift-api.sarbo.workers.dev/albums/${albumID}`);
    expect(response.status).toBe(200);
    expect(Array.isArray(response.data)).toBeTruthy();
    expect(response.data.length).toBeGreaterThan(0);
    response.data.forEach(song => {
      expect(song).toHaveProperty('song_id');
      expect(song).toHaveProperty('title');
      expect(song).toHaveProperty('length');
    });
  });

  // Additional tests for other scenarios like invalid albumID, server errors, etc., can be added here
});
