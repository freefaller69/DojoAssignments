import { TimezonesPage } from './app.po';

describe('timezones App', () => {
  let page: TimezonesPage;

  beforeEach(() => {
    page = new TimezonesPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
