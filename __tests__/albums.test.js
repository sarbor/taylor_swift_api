const axios = require('axios');

jest.mock('axios');

describe('Albums endpoint', () => {
  test('GET /albums should return status code 200 and an array of albums', async () => {
    const mockAlbums = [
      { album_id: '1', title: 'Fearless', release_date: '2008-11-11' },
      { album_id: '2', title: 'Speak Now', release_date: '2010-10-25' },
      // ... other albums
    ];

    jest.spyOn(axios, 'get').mockResolvedValue({
      status: 200,
      data: mockAlbums
    });

    const response = await axios.get('https://taylor-swift-api.sarbo.workers.dev/albums');
    expect(response.status).toBe(200);
    expect(Array.isArray(response.data)).toBeTruthy();
    expect(response.data.length).toBeGreaterThan(0);
    response.data.forEach(album => {
      expect(album).toHaveProperty('album_id');
      expect(album).toHaveProperty('title');
      expect(album).toHaveProperty('release_date');
    });
  });
});
