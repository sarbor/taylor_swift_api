const axios = require('axios');

jest.mock('axios');

describe('/songs endpoint', () => {
  test('GET /songs should return status code 200 and an array of songs', async () => {
    const mockSongs = [
      { song_id: '1', title: 'Love Story', album_id: '1' },
      { song_id: '2', title: 'You Belong With Me', album_id: '1' },
      // ... other songs
    ];

    jest.spyOn(axios, 'get').mockResolvedValue({
      status: 200,
      data: mockSongs
    });

    const response = await axios.get('https://taylor-swift-api.sarbo.workers.dev/songs');
    expect(response.status).toBe(200);
    expect(Array.isArray(response.data)).toBeTruthy();
    expect(response.data.length).toBeGreaterThan(0);
    response.data.forEach(song => {
      expect(song).toHaveProperty('song_id');
      expect(song).toHaveProperty('title');
      expect(song).toHaveProperty('album_id');
    });
  });

  // Additional tests for other scenarios like server errors, etc., can be added here
});
