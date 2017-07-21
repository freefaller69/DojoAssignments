import { ForecastPage } from './app.po';

describe('forecast App', () => {
  let page: ForecastPage;

  beforeEach(() => {
    page = new ForecastPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
