import { QuoteRanksProjectPage } from './app.po';

describe('quote-ranks-project App', () => {
  let page: QuoteRanksProjectPage;

  beforeEach(() => {
    page = new QuoteRanksProjectPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
