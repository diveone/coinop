class CoinView extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            coins: [],
            loading: true,
            currentPage: 1,
            coinsPerPage: 50,
            totalPages: 1,
            pager: {}
        };

        this.getPages = this.getPages.bind(this);
        this.createPageItems = this.createPageItems.bind(this);
    }

    componentWillMount() {
        fetch('/api/latest')
            .then(response => response.json())
            .then(json => {
                this.setState({
                    coins: json[0],
                    loading: false })
            })
            .catch(err => console.error(err))
    }

    componentDidMount() {
        let pages = this.getPages();
        this.setState({
            totalPages: pages })
    }

    createCoinElements() {
        let { coins, pager, currentPage } = this.state;
        let coinPages = pager[currentPage];
        return coins.map((coin) => {
            return <Coin key={coin.id} {...coin} />
        })
    }

    getPages() {
        const { coins, coinsPerPage, pager, currentPage } = this.state;
        console.log('getPages', coins.length);
        const totalPages = Math.ceil(coins/coinsPerPage);
        if (!pager) {
            let pageCount = 0;
            let start = 0;
            for (let i =1; i <= totalPages; i++) {
                pageCount += coinsPerPage;
                pager[i] = coins.slice(start, pageCount);
                start += coinsPerPage;
            }

            this.setState({ pager: pager, coins: pager[currentPage], totalPages: totalPages});
        }
        return totalPages
    }

    createPageItems() {
        const { totalPages } = this.state;
        const pageItems = [];
        for (let i = 1; i <= totalPages; i++) {
            pageItems.push(i)
        }

        return pageItems.map((num) => {
            return <div key="${num}" className="page-item" onClick={this.handlePage}>${num}</div>
        })
    }

    handlePage(e) {
        const page = e.target.id;
        let coinsRange = pager[page];

        const coins = coins.slice(...coinsRange).map((coin) => {
            return <Coin key={coin.id} {...coin} />
        });

        // Update state currentPage
        this.setState({ currentPage: e.target.id });
        // Set className to active
        e.target.className += 'active';
        // render
        this.setState({ coins });

    }

    render() {
        const coins = this.createCoinElements();
        const { loading, coinsPerPage, currentPage, totalPages } = this.state;
        const pageItems = this.createPageItems();
        console.log(pageItems);

        return (
            <div>
                <Navigation />
                <div className="container">
                    <div className="pagination pagination-lg">
                        { pageItems }
                    </div>
                    <div className="list-group">
                        { loading ? <progress></progress> : coins }
                    </div>
                </div>
            </div>
        )
    }
}
