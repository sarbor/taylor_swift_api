const axios = require('axios');

jest.mock('axios');

describe('/songs/{songID} endpoint', () => {
  test('GET /songs/{songID} with a valid songID should return status code 200 and a song object', async () => {
    const songID = '1';
    const mockSong = {
      song_id: songID,
      title: 'Love Story',
      album_id: '1',
      length: '3:55'
    };

    jest.spyOn(axios, 'get').mockResolvedValue({
      status: 200,
      data: mockSong
    });

    const response = await axios.get(`https://taylor-swift-api.sarbo.workers.dev/songs/${songID}`);
    expect(response.status).toBe(200);
    expect(response.data).toHaveProperty('song_id');
    expect(response.data).toHaveProperty('title');
    expect(response.data).toHaveProperty('album_id');
    expect(response.data).toHaveProperty('length');
  });

  // Additional tests for other scenarios like invalid songID, server errors, etc., can be added here
});
